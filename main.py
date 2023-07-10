import sys
import os
from pixel import PixelArtConverter

# Get command line argument
path = sys.argv[1]

# If path is a directory, get all files in the directory.
# If path is a file, use the file.
if os.path.isdir(path):
    picture_paths = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
else:
    picture_paths = [path]

# Convert all images
converter = PixelArtConverter(picture_paths)
converter.convert_to_hex()

# Set to hold all unique colors
all_unique_colors = set()

for i, pixels in enumerate(converter.pixel_data):
    unique_colors = set()
    for pixel in pixels:
        unique_colors.add(pixel['color'])
        all_unique_colors.add(pixel['color'])

    print(f"Picture {i+1} ({picture_paths[i]}):")
    print("Hex Codes used:")
    for color in unique_colors:
        print(color)

# Map all unique colors to .c## format and print
print("All unique colors:")
for i, color in enumerate(sorted(list(all_unique_colors))):
    print(f".c{i:02d}{{fill:{color}}}")
