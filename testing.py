from ultralytics import YOLO
import numpy as np
from PIL import Image
import os
import cv2  # OpenCV for HSV processing

# Load the trained YOLO model
model = YOLO("./best.pt")

# Specify the source image path
source_image_path = "./2.jpg"

# Perform inference
results = model.predict(source=source_image_path, save=True)  # Save=True to save the predictions overlay

# Load the source image
image = Image.open(source_image_path).convert("RGBA")  # Ensure the image has an alpha channel
image_np = np.array(image)  # Convert to NumPy array for OpenCV processing

# Convert the image to HSV using OpenCV
image_hsv = cv2.cvtColor(image_np[:, :, :3], cv2.COLOR_RGB2HSV)  # Exclude alpha channel

# Output directory for segmented images
output_dir = "segmented_images"
os.makedirs(output_dir, exist_ok=True)

# Get the original image dimensions
original_width, original_height = image.size

# Define HSV range for filtering (example: red color)
lower_hsv = np.array([0, 25, 25])    # Adjusted range for more general red tones
upper_hsv = np.array([80, 255, 255]) 

# Process the segmentation masks
for i, mask in enumerate(results[0].masks.data):  # Loop through segmentation masks
    # Convert mask tensor to a binary NumPy array
    mask_array = (mask.cpu().numpy() * 255).astype(np.uint8)

    # Create a PIL mask image (binary mask)
    mask_image = Image.fromarray(mask_array, mode="L")

    # Resize the mask to match the original image size
    mask_image_resized = mask_image.resize((original_width, original_height), Image.NEAREST)

    # Apply the mask to the original image
    mask_np_resized = np.array(mask_image_resized)  # Convert to NumPy for masking
    if len(mask_np_resized.shape) == 2:
        mask_np_resized = cv2.merge([mask_np_resized, mask_np_resized, mask_np_resized])

    masked_hsv = cv2.bitwise_and(image_hsv, mask_np_resized)

    # Apply HSV filtering
    filtered_hsv = cv2.inRange(masked_hsv, lower_hsv, upper_hsv)  # Binary mask for HSV range

    # Convert filtered mask back to an image
    filtered_hsv_colored = cv2.cvtColor(filtered_hsv, cv2.COLOR_GRAY2BGR)  # Convert binary mask to 3-channel for saving
    segmented_image = cv2.bitwise_and(image_np[:, :, :3], filtered_hsv_colored)

    # Save the HSV-processed segmented image
    segmented_image_path = os.path.join(output_dir, f"segmented_hsv_{i}.png")
    Image.fromarray(segmented_image).save(segmented_image_path)
    print(f"HSV-processed segmented image saved to: {segmented_image_path}")
