from PIL import Image
import os

# Load the image
 # replace with your image path
image_path = 'image.png' 
img = Image.open(image_path)

# Create an output directory for sliced images
output_dir = 'sliced_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get the size of the image
img_width, img_height = img.size

# Set slice size
slice_width = 1
slice_height = 600

# Calculate number of slices along width and height
num_slices_x = img_width // slice_width
num_slices_y = img_height // slice_height

# Slice the image
for i in range(num_slices_x):
    for j in range(num_slices_y):
        left = i * slice_width
        upper = j * slice_height
        right = left + slice_width
        lower = upper + slice_height
        slice_box = (left, upper, right, lower)

        # Create and save the slice
        slice_img = img.crop(slice_box)
        slice_img.save(os.path.join(output_dir, f'slice_{i}_{j}.png'))

print("Image slicing completed!")
