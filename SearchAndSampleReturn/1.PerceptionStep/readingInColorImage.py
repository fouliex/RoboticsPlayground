# import some packages from matplotlib
import matplotlib.image as mpimp
import matplotlib.pyplot as plt
import numpy as np

'''
Image is stored as an array and we can perform operation on it.
We can explore what it's size and datatype are, as well as the minimum and maximum values
in the array using the numpy package
'''
# Define the filename, read and plot the image
filename = 'sample.jpg'
image = mpimp.imread(filename)
plt.imshow(image)
# plt.show()

'''
Here we can see it's an 8-bit unsigned integer array(unint8),where the size of the array is (160,320,3)
meaning that the image size is 160 pixels in the y-direction(height),320 pixels in the x-direction(width) and it has
3 layers or "color channels".

We can also see that the minimum and maximum values are 0 and 255, respectively. This comes from the fact that with
8 bits of information for each pixel in each color channel, you have 2^​8. or 256 possible values, with the minimum
possible value being 0 and the maximum being 255.
Not all images are scaled this way so it's always a good idea to check the range and data type of the array after 
reading in an image if you're not sure.

The three color channels of the image are red, green and blue or "RGB" for short. The combination of intensity values
 across the three channels determines what color we see in the image. 
'''
# uint8 (160, 320, 3) 0 255
print(image.dtype, image.shape, np.min(image), np.max(image))

# we can look at each of the color channels in isolation by zeroing out the others and lining them up side by side
#
red_channel = np.copy(image)
red_channel[:, :, [1, 2]] = 0  # Zero out the green(1) and blue(2) channels
green_channel = np.copy(image)
green_channel[:, :, [0, 2]] = 0  # Zero out the red(0) and blue

blue_channel = np.copy(image)
blue_channel[:, :, [0, 1]] = 0  # Zero out the red(0) and green(1)

fig = plt.figure(figsize=(12, 3))
plt.subplot(131)
plt.imshow(red_channel)
plt.subplot(132)
plt.imshow(green_channel)
plt.subplot(133)
plt.imshow(blue_channel)
plt.show()
