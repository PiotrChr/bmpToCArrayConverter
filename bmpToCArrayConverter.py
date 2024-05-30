import sys
from PIL import Image

def image_to_c_array(image_path):
    with Image.open(image_path) as image:
        bw = image.convert('1').point(lambda x: 0 if x == 0 else 1, '1')
    
        pixels = bw.load()
        
        byte_array = []
        for y in range(64):  # height
            for byte_index in range(16):  # width divided by 8
                byte_value = 0
                for bit_index in range(8):  # 8 bits per byte
                    x = byte_index * 8 + bit_index
                    # Invert the bit logic if needed (1 for black, 0 for white)
                    if pixels[x, y] == 0:
                        byte_value |= (1 << (7 - bit_index))
                byte_array.append(byte_value)
                
        return byte_array

def format_c_array(byte_array):
    # Format the byte array as a C array with PROGMEM attribute
    formatted_bytes = ', '.join(f'0x{b:02x}' for b in byte_array)
    return f'const unsigned char logov1[1024] PROGMEM = {{\n  {formatted_bytes}\n}};'

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    try:
        byte_array = image_to_c_array(image_path)
        c_array_code = format_c_array(byte_array)
        print(c_array_code)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

