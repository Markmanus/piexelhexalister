from PIL import Image

class PixelArtConverter:
    def __init__(self, picture_paths):
        self.picture_paths = picture_paths
        self.pixel_data = []

    def convert_to_hex(self):
        for picture_path in self.picture_paths:
            img = Image.open(picture_path)
            width, height = img.size
            pixels = []

            for y in range(height):
                for x in range(width):
                    pixel_color = img.getpixel((x, y))
                    hex_color = self.rgb_to_hex(pixel_color)
                    pixel_info = {
                        'x': x,
                        'y': y,
                        'color': hex_color
                    }
                    pixels.append(pixel_info)

            self.pixel_data.append(pixels)

    @staticmethod
    def rgb_to_hex(rgb):
        hex_color = '#{:02x}{:02x}{:02x}'.format(*rgb)
        return hex_color

# Example usage

