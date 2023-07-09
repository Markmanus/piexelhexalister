from pixel import PixelArtConverter
from PIL import Image
from pandas import DataFrame

# Example usage
picture_paths = ["pixelart.png", "pixelart2.png"]
converter = PixelArtConverter(picture_paths)
converter.convert_to_hex()

for i, pixels in enumerate(converter.pixel_data):
    print(f"Picture {i+1}:")
    for pixel in pixels:
        print(f"Coordinates: ({pixel['x']}, {pixel['y']}) - Color: {pixel['color']}")

