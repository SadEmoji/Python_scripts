
from PIL import Image
import csv

input_file = "http/solid.png"
output_file = "non_white_pixels.csv"

image = Image.open(input_file).convert("RGBA")

width, height = image.size
count = 0

with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["X", "Y", "R", "G", "B", "A"])

    for y in range(height):
        for x in range(width):
            r, g, b, a = image.getpixel((x, y))

            # Skip pure white pixels
            if (r, g, b) != (255, 255, 255):
                writer.writerow([x, y, r, g, b, a])
                count += 1

print(f"Image size: {width}x{height}")
print(f"Non-white pixels saved: {count}")
print(f"CSV saved to: {output_file}")
