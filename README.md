# File-to-Image and Image-to-File Converter

This repository contains two Python scripts that allow you to convert a file to an image and back from an image to a file. 

## Usage

### Convert File to Image (fti)

To convert a file to an image, use the fti function with the path to the input file and the desired output image path:

```fti('inputfile.bin', 'outputimage.png')```

### Convert Image to File (itf)

To convert an image back to a file, use the itf function with the path to the input image and the desired output file path:

```itf('inputimage.png', 'outputfile.bin')```

## Requirements

To run these scripts, you need to have Python installed along with the Pillow library. You can install Pillow using pip:

```pip install pillow```

## Explanation of How It Works:

Convert File to Image (fti):

The fti function operates as follows:
1. Read the File: The script reads the entire file in binary mode.
2. Convert to Binary: The binary data is converted into a string of bits.
3. Calculate Image Size: The size of the image is determined based on the number of bits.
4. Create Image: An RGBA image of the calculated size is created with a white background and fully transparent alpha channel.
5. Embed Data: The number of bits is stored in the first 32 bits of the image. Then, each bit of the file's binary data is stored in the alpha channel of each pixel, making it either fully transparent (0) or fully opaque (255).
6. Save Image: The image is saved to the specified output path.

Convert Image to File (itf):

The itf function operates as follows:
1. Open the Image: The script opens the image and accesses its pixels.
2. Extract Bits: It extracts the bits from the alpha channel of each pixel. A value greater than 128 is considered '1', otherwise '0'.
3. Determine Data Length: The first 32 bits represent the length of the original binary data.
4. Reconstruct Binary Data: The remaining bits are collected based on the original data length.
5. Write to File: The binary data is converted back to bytes and written to the specified output file.

These scripts provide a method to encode binary data into an image and decode it back, ensuring data integrity throughout the process.
