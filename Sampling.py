# -*- coding: utf-8 -*-
"""
@author: Anthony DiBenedetto
"""

import numpy as np
from skimage import data
from matplotlib import pyplot as plt
from PIL import Image

path = "/Users/anthonydibenedetto/Desktop/PIA19247_modest.jpg"

# Load a sample image from skimage
image = Image.open(path) 
image = np.array(image)

# Display the shape and type of the loaded image
print(type(image))

# Define the ratio for downscaling the image
# The higher the ratio, the lower the resolution of the output image
ratio = 30  

def sampling(image, ratio=20, show_image=True):
    """
    Reduces the resolution of the given image using mean sampling method.

    Parameters:
    - image: The original image as a numpy array.
    - ratio: The factor by which the image resolution should be reduced.
    - show_image: A boolean to decide whether to display the images.

    The function creates a new image array with reduced dimensions.

    Returns:
    - new_image: The downsampled image as a numpy array.
    """

    # Initialize an empty array for the new image with reduced dimensions
    new_image = np.zeros((int(image.shape[0]/ratio),
                          int(image.shape[1]/ratio),
                          image.shape[2]), dtype='float32')

    # Iterate over each pixel block to compute the mean value
    for i in range(new_image.shape[0]):
        for j in range(new_image.shape[1]):
            for k in range(new_image.shape[2]):
                # Extract the block of pixels
                delta = image[i*ratio:(i+1)*ratio, j*ratio:(j+1)*ratio, k]
                # Assign the mean value to the new image
                new_image[i, j, k] = np.mean(delta)
                
    # Display the original and downsampled images if show_image is True
    if show_image:
        plt.imshow(new_image.astype('uint8'))
        plt.show()
        plt.imshow(image)
        plt.show()

    return new_image

sampling(image, ratio=ratio)
