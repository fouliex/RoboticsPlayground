import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


from lib.dependencies import perspect_transform, color_thresh, rover_coords


# Apply a rotation to pixel positions by mapping
# rover space pixels to world space
def rotate_pix(xpix, ypix, yaw):
    # Convert yaw to radians
    yaw_rad = yaw * np.pi / 180
    xpix_rotated = (xpix * np.cos(yaw_rad)) - (ypix * np.sin(yaw_rad))
    ypix_rotated = (xpix * np.sin(yaw_rad)) + (ypix * np.cos(yaw_rad))
    return xpix_rotated, ypix_rotated


def translate_pix(xpix_rot, ypix_rot, xpos, ypos, scale):
    # Apply a scaling and a translation
    xpix_translated = (xpix_rot / scale) + xpos
    ypix_translated = (ypix_rot / scale) + ypos
    return xpix_translated, ypix_translated


# Apply rotation and translation( and clipping)
def pix_to_world(xpix, ypix, xpos, ypos, yaw, world_size, scale):
    # Apply rotation
    xpix_rot, ypix_rot = rotate_pix(xpix, ypix, yaw)
    # Apply translation
    xpix_tran, ypix_tran = translate_pix(xpix_rot, ypix_rot, xpos, ypos, scale)
    # Clip to world_size
    x_pix_world = np.clip(np.int_(xpix_tran), 0, world_size - 1)
    y_pix_world = np.clip(np.int_(ypix_tran), 0, world_size - 1)
    # Return the result
    return x_pix_world, y_pix_world


if __name__ == '__main__':
    # Read in the sample image
    image = mpimg.imread('sample.jpg')

    # Rover yaw values will come as floats from 0 to 360
    # Generate a random value in this range
    rover_yaw = np.random.random(1) * 160 + 20

    # Generate a random rover position in world coords
    # Position values will range from 20 to 180 to
    # avoid the edges in  a 200 x 200 pixel world
    rover_xpos = np.random.random(1) * 160 + 20
    rover_ypos = np.random.random(1) * 160 + 20

    # perform warping
    warped = perspect_transform(image)

    # perform  color thresholding
    colorsel = color_thresh(warped, rgb_thresh=(160, 160, 160))

    # Extract navigable terrain pixels
    xpix, ypix = rover_coords(colorsel)

    # Generate 200 x 200 pixel worldmap
    worldmap = np.zeros((200, 200))
    scale = 10
    # Get navigable pixel positons in world coords
    x_world, y_world = pix_to_world(xpix, ypix, rover_xpos, rover_ypos, rover_yaw, worldmap.shape[0], scale)

    # Add pixel positions to worldmap
    worldmap[y_world, x_world] += 1
    print('Xpos =', rover_xpos, 'Ypos =', rover_ypos, 'Yaw =', rover_yaw)

    # Plot the map in rover-centric coords
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    f.tight_layout()
    ax1.plot(xpix, ypix, '.')
    ax1.set_title('Rover Space', fontsize=40)
    ax1.set_ylim(-160, 160)
    ax1.set_xlim(0, 160)
    ax1.tick_params(labelsize=20)

    ax2.imshow(worldmap, cmap='gray')
    ax2.set_title('World Space', fontsize=40)
    ax2.set_ylim(0, 200)
    ax2.tick_params(labelsize=20)
    ax2.set_xlim(0, 200)

    plt.subplots_adjust(left=0.1, right=1, top=0.9, bottom=0.1)
    plt.show()
