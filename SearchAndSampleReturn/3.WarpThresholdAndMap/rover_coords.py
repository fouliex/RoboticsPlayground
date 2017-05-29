import matplotlib.pyplot as plt
import numpy as np
import cv2
import matplotlib.image as mpimg

# Read in the sample image
image = mpimg.imread('sample.jpg')


def perspective_transform(img, src, dst):
    m = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, m, (img.shape[1], img.shape[0]))
    return warped


def color_thresh(img, rgb_thresh=(160, 160, 160)):
    color_select = np.zeros_like(img[:, :, 0])
    above_thresh = (img[:, :, 0] > rgb_thresh[0]) & (img[:, :, 1] > rgb_thresh[1]) & (img[:, :, 2] > rgb_thresh[2])
    color_select[above_thresh] = 1
    return color_select


# Define calibration box in source (actual) and destination (desired) coordinates
# These source and destination points are defined to warp the image
# to a grid where each 10x10 pixel square represents 1 square meter
dst_size = 5
# Set a bottom offset to account for the fact that the bottom of the image
# is not the position of the rover but a bit in front of it
bottom_offset = 6
source = np.float32([[14, 140], [301, 140], [200, 96], [118, 96]])
destination = np.float32([[image.shape[1] / 2 - dst_size, image.shape[0] - bottom_offset],
                          [image.shape[1] / 2 + dst_size, image.shape[0] - bottom_offset],
                          [image.shape[1] / 2 + dst_size, image.shape[0] - 2 * dst_size - bottom_offset],
                          [image.shape[1] / 2 - dst_size, image.shape[0] - 2 * dst_size - bottom_offset],
                          ])

'''
Convert from image coordinate to rover coordinate
'''


def rover_coords(binary_img):
    # Identify nonzero pixels
    ypos, xpos = binary_img.nonzero()

    x_pixel = -(ypos - binary_img.shape[0]).astype(np.float)
    y_pixel = -(xpos - binary_img.shape[1] / 2).astype(np.float)
    return x_pixel, y_pixel


def plot_rover_centric_coords_map(xpix, ypix):
    fig = plt.figure(figsize=(5, 7.5))
    plt.plot(xpix, ypix, '.')
    plt.ylim(-160, 160)
    plt.xlim(0, 160)
    plt.title('Rover_Centric Map', fontsize=20)
    plt.show()


if __name__ == '__main__':
    # Perform warping and color thresholding
    warped = perspective_transform(image, source, destination)
    colorsel = color_thresh(warped, rgb_thresh=(160, 160, 160))

    # Extract x and y positions of navigable terrain pixels
    # and convert to rover coordinates
    xpix, ypix = rover_coords(colorsel)
    plot_rover_centric_coords_map(xpix, ypix)
