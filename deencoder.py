from PIL import Image

def itf(ipath, outputf):
    image = Image.open(ipath)
    pixels = image.load()
    
    image_size = image.size[0]
    
    bits = ''
    for y in range(image_size):
        for x in range(image_size):
            alpha_value = pixels[x, y][3]  
            bits += '1' if alpha_value > 128 else '0'  

    size_bits = bits[:32]
    num_bits = int(size_bits, 2)

    bits = bits[32:32+num_bits]

    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        byte_array.append(int(byte, 2))
    
    with open(outputf, 'wb') as file:
        file.write(byte_array)
    
    print(f"Archivo guardado en {outputf}")

