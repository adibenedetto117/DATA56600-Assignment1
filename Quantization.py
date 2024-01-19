# -*- coding: utf-8 -*-
"""
@author: Anthony DiBenedetto
"""
from skimage import data
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

path = "/Users/anthonydibenedetto/Desktop/PIA19247_modest.jpg"

# Load a sample image from skimage
image = Image.open(path)

# Show the original image
print("Original image:")
plt.imshow(image)
plt.show()

# Set the quantization ratio
# A higher ratio results in fewer colors in the quantized image
ratio = 100

def quantization(image, ratio):
    """
    Apply quantization to the given image with the specified ratio.

    Parameters:
    - image: The original image as a numpy array.
    - ratio: The quantization ratio.

    This function modifies the original image array in place, reducing the color depth.

    Returns:
    - image: The quantized image as a numpy array.
    """
    # Iterate over each pixel in the image
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(image.shape[2]):
                # Apply quantization by modifying the pixel's color value
                image[i][j][k] = int(image[i][j][k] / ratio) * ratio

    return image

# Apply quantization to the image
quantized_image = quantization(np.copy(image), ratio)

# Show the quantized image
print("Quantized image:")
plt.imshow(quantized_image)
plt.show()

# Print the shape of the quantized image
print("Shape of the quantized image:", np.shape(quantized_image))
