from PIL import Image
import math

def fti(path, output):
    with open(path, 'rb') as file:
        data = file.read()
    
    bits = ''.join(format(byte, '08b') for byte in data)

    num_bits = len(bits)
    size = int(math.ceil((num_bits + 32)**0.5)) 

    image = Image.new('RGBA', (size, size), color=(255, 255, 255, 0))
    pixels = image.load()

    size_bits = format(num_bits, '032b')
    bits = size_bits + bits

    for i in range(len(bits)):
        x = i % size
        y = i // size
        alpha_value = int(bits[i]) * 255 
        pixels[x, y] = (255, 255, 255, alpha_value)  

    image.save(output)
    print(f"Image saved in {output}")

