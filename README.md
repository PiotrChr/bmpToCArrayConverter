# Image to C Array Converter

This Python script converts a bitmap image to a C-style array suitable for embedded programming, specifically formatted to be stored in program memory (PROGMEM). It is designed to process 64x128 pixel black and white images and output a C array representing the image data where each bit corresponds to a pixel (1 for black, 0 for white).

## Requirements

- Python 3
- Pillow library

## Installation

Install the required Python package Pillow using pip:
```bash
pip install Pillow
```

## Usage

Run the script from the command line by specifying the path to the image file:
```bash
python script.py <image_path>
```

Ensure that the image is 64x128 pixels in size and in a format supported by Pillow (e.g., BMP, PNG, JPEG).

## How It Works

1. **Image Loading:** The script loads the image from the specified file path.
2. **Conversion to Black and White:** The image is converted to a black and white (1-bit) format.
3. **Array Conversion:** The script iterates over each pixel and constructs a byte array, where each byte represents eight pixels.
4. **C Array Formatting:** The byte array is then formatted into a C array declaration with the `PROGMEM` attribute, making it ready to use in AVR C programming environments for devices like Arduino.

## Output

The script outputs a C array of hexadecimal bytes that can be directly embedded into C code for AVR or similar microcontrollers.

## Note

This script does not perform image scaling or cropping. Ensure that the input image is exactly 64x128 pixels. Incorrect dimensions will lead to improper array formatting or script errors.
