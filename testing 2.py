from ultralytics import YOLO
import numpy as np
from PIL import Image
import os
import cv2
from picamera import PiCamera
from time import sleep

camera = PiCamera()

def get_next_filename(directory, prefix, extension):
    i = 0
    while os.path.exists(os.path.join(directory, f"{prefix}_{i}.{extension}")):
        i += 1
    return os.path.join(directory, f"{prefix}_{i}.{extension}")

model = YOLO("./best.pt")
output_dir = "segmented_images"
os.makedirs(output_dir, exist_ok=True)

lower_hsv = np.array([0, 25, 25])
upper_hsv = np.array([80, 255, 255])

try:
    while True:
        image_path = get_next_filename(".", "image", "jpg")
        camera.start_preview()
        sleep(2)
        camera.capture(image_path)
        camera.stop_preview()

        results = model.predict(source=image_path, save=True)
        image = Image.open(image_path).convert("RGBA")
        image_np = np.array(image)
        image_hsv = cv2.cvtColor(image_np[:, :, :3], cv2.COLOR_RGB2HSV)

        original_width, original_height = image.size

        for i, mask in enumerate(results[0].masks.data):
            mask_array = (mask.cpu().numpy() * 255).astype(np.uint8)
            mask_image = Image.fromarray(mask_array, mode="L")
            mask_image_resized = mask_image.resize((original_width, original_height), Image.NEAREST)
            mask_np_resized = np.array(mask_image_resized)
            if len(mask_np_resized.shape) == 2:
                mask_np_resized = cv2.merge([mask_np_resized, mask_np_resized, mask_np_resized])

            masked_hsv = cv2.bitwise_and(image_hsv, mask_np_resized)
            filtered_hsv = cv2.inRange(masked_hsv, lower_hsv, upper_hsv)
            filtered_hsv_colored = cv2.cvtColor(filtered_hsv, cv2.COLOR_GRAY2BGR)
            segmented_image = cv2.bitwise_and(image_np[:, :, :3], filtered_hsv_colored)

            segmented_image_path = get_next_filename(output_dir, "segmented_hsv", "png")
            Image.fromarray(segmented_image).save(segmented_image_path)
            print(f"HSV-processed segmented image saved to: {segmented_image_path}")

        original_image_path = get_next_filename(output_dir, "original", "png")
        image.save(original_image_path)
        print(f"Original image saved to: {original_image_path}")

        hsv_image_path = get_next_filename(output_dir, "hsv", "png")
        Image.fromarray(image_hsv).save(hsv_image_path)
        print(f"HSV image saved to: {hsv_image_path}")

except KeyboardInterrupt:
    print("Program terminated by user.")
    
    