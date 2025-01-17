from ultralytics import YOLO
import numpy as np
from PIL import Image
import os

model = YOLO("./best.pt")
source_image_path = "./2.jpg"
results = model.predict(source=source_image_path, save=True) 
image = Image.open(source_image_path).convert("RGBA")
output_dir = "segmented_images"
os.makedirs(output_dir, exist_ok=True)
original_width, original_height = image.size

for i, mask in enumerate(results[0].masks.data):
    mask_array = (mask.cpu().numpy() * 255).astype(np.uint8)
    mask_image = Image.fromarray(mask_array, mode="L")
    mask_image_resized = mask_image.resize((original_width, original_height), Image.NEAREST)
    segmented_image = Image.composite(
        image, 
        Image.new("RGBA", image.size, (255, 255, 255, 0)), 
        mask_image_resized
    )
    segmented_image_path = os.path.join(output_dir, f"segmented_{i}.png")
    segmented_image.save(segmented_image_path)
    print(f"Segmented image saved to: {segmented_image_path}")
