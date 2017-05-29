import matplotlib.image as mping
import matplotlib.pyplot as plt
import cv2
import numpy as np

image = mping.imread("example_grid1.jpg")
plt.imshow(image)
plt.show()


# Get transform matrix using cv2.getPerspectiveTransform()
def perspectTransform(img, src, dst):
    M = cv2.getPerspectiveTransform(src, dst)
    wraped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    return wraped


# Define source and destination points
source = np.float32([[0, 0], [0, 0], [0, 0], [0, 0]])
destination = np.float32([[0, 0], [0, 0], [0, 0], [0, 0]])

warped = perspectTransform(image, source, destination)
plt.imshow(warped)
plt.show()
