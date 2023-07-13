# Pixel Art Hex Color Code Extractor

This is a Python tool that extracts unique hex color codes from pixel art images. The extracted colors are output in the format `.c##{fill:#xxxxxx}`, where `##` is a two-digit number and `xxxxxx` is the hex color code. If multiple images are processed, the color codes across all images are combined and presented.

## Setup (python3)

1. Clone the repository:
    ```bash
    git clone https://github.com/0xcircuitbreaker/pixel-hex-lister.git
    cd pixel-hex-lister
    ```

2. Install the required dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

There are two ways to use this tool:

1. Processing a single image:
    ```bash
    python3 main.py pixelart.png
    ```

2. Processing all images in a directory:
    ```bash
    python3 main.py pixelart
    ```

In both cases, the unique hex color codes from the images will be printed to the console.

## Testing

For testing, a single image file (`pixelart.png`) and a directory (`pixelart/`) containing a single image are included in the working directory.

## Contributing

If you have suggestions for improvements, or want to report a bug, open an issue! All contributions are welcome.

## License

For more information about the license of this project, please see the [LICENSE](./LICENSE) file.

## Acknowledgements

Thanks to the Python and Pillow projects for the open-source software that made this tool possible.
