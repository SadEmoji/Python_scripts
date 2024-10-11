import os
import random
from PIL import Image

# Folder containing your images
image_folder = 'input'
output_folder = 'output'

# Get the list of all images
image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith(('png', 'jpg', 'jpeg'))]

# Make sure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Load all the images
images = [Image.open(img) for img in image_files]

# Ensure all images are the same height and width
width, height = 1, 600

# Create x random combinations
for i in range(800):
    # Shuffle the images randomly
    random.shuffle(images)
    
    # Create a new blank image with 800px width and 600px height
    new_image = Image.new('RGB', (800, height))
    
    # Paste each image into the new image
    for idx, img in enumerate(images):
        new_image.paste(img, (idx, 0))  # Paste at x = idx, y = 0
    
    # Save the new image
    new_image.save(os.path.join(output_folder, f'random_image_{i+1}.png'))

print("random images created")
