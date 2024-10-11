import os
from PIL import Image
import numpy as np

# Function to calculate the percentage of white pixels in an image
def calculate_white_percentage(image):
    image = image.convert('RGB')  # Ensure the image is in RGB format
    np_image = np.array(image)
    
    # Define white as pixels with RGB values close to (255, 255, 255)
    white_threshold = 240  # You can adjust this threshold for more or less whiteness
    white_pixels = np.sum(np.all(np_image >= white_threshold, axis=-1))
    
    total_pixels = np_image.shape[0] * np_image.shape[1]
    white_percentage = (white_pixels / total_pixels) * 100
    
    return white_percentage

# Function to calculate total white pixel continuity between two images
def white_continuity(img1, img2):
    # Get the right edge of img1 and left edge of img2
    img1_right_edge = np.array(img1.convert('RGB'))[:, -1, :]
    img2_left_edge = np.array(img2.convert('RGB'))[:, 0, :]
    
    # Check how similar the white pixels are along the adjacent edges
    continuity = np.sum(np.all((img1_right_edge >= 240) & (img2_left_edge >= 240), axis=-1))
    
    return continuity

# Function to calculate continuity for entire adjacent areas (more robust)
def total_white_continuity(img1, img2):
    img1_right_half = np.array(img1.convert('RGB'))[:, int(img1.width/2):, :]
    img2_left_half = np.array(img2.convert('RGB'))[:, :int(img2.width/2), :]
    
    # Compare white pixels across the two regions
    continuity = np.sum(np.all((img1_right_half >= 240) & (img2_left_half >= 240), axis=-1))
    
    return continuity

# Function to find the best image based on white continuity and look ahead
def find_best_next_image(last_image, candidates):
    best_score = -1
    best_index = -1

    for i, candidate in enumerate(candidates):
        next_image = candidate[0]
        
        # Consider both edge and overall white pixel continuity
        continuity_score = white_continuity(last_image, next_image)
        overall_continuity = total_white_continuity(last_image, next_image)
        
        # Combine the scores with a weight to prefer smooth transitions
        score = continuity_score + overall_continuity

        if score > best_score:
            best_score = score
            best_index = i
    
    return best_index

# Folder containing your images
image_folder = 'input'
output_folder = 'whiteout'

# Get the list of all images
image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith(('png', 'jpg', 'jpeg'))]

# Make sure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Load all the images and calculate their white pixel percentage
images_with_white_percentage = []
for img_path in image_files:
    img = Image.open(img_path)
    white_percentage = calculate_white_percentage(img)
    images_with_white_percentage.append((img, white_percentage))

# Sort the images by the percentage of white pixels (descending order)
images_with_white_percentage.sort(key=lambda x: x[1], reverse=True)

# Start with the image that has the most white pixels
arranged_images = [images_with_white_percentage.pop(0)[0]]

# Iteratively add images that have the highest white continuity
while images_with_white_percentage:
    last_image = arranged_images[-1]
    
    # Find the best matching image based on white pixel continuity
    best_match_idx = find_best_next_image(last_image, images_with_white_percentage)
    
    # Add the best matching image to the arrangement
    arranged_images.append(images_with_white_percentage.pop(best_match_idx)[0])

# Create the final image by arranging images with continuous white areas
# Set size of image
new_image = Image.new('RGB', (800, 600))

# Paste images according to their calculated white continuity
for idx, img in enumerate(arranged_images):
    new_image.paste(img, (idx, 0))  # Paste image horizontally

# Save the arranged image
new_image.save(os.path.join(output_folder, 'arranged_by_white.png'))

print("Sorted image saved")
