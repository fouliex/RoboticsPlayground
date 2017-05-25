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
filename ='sample.jpg'
image = mpimp.imread(filename)
plt.imshow(image)
plt.show()


'''

'''
# uint8 (160, 320, 3) 0 255
print(image.dtype,image.shape,np.min(image),np.max(image))
