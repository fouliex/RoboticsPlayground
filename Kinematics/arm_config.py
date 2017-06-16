import matplotlib.pyplot as plt
import numpy as np


# Define a function to computer the arm configuration
def compute_arm_config(link1_length, link2_length, joint0_angle, joint1_angle):
    joint1_x = 0
    joint1_y = 0
    p2_x = 0
    p2_y = 0
    return joint1_x, joint1_y, p2_x, p2_y


if __name__ == '__main__':
    # Generate random link lengths and joint angles
    # Note: because these are randomly generated on each run
    link1_length = np.random.random() * 30 + 20
    link2_length = np.random.random() * 30 + 20
    joint0_angle = np.random.random() * 2 * np.pi
    joint1_angle = np.random.random() * 2 * np.pi
    joint1_x, joint1_y, p2_x, p2_y = compute_arm_config(link1_length, link2_length, joint0_angle, joint1_angle)

    print("joint0_angle = ", round(joint0_angle * 180 / np.pi, 1), "degrees")
    print("joint1_angle = ", round(joint1_angle * 180 / np.pi, 1), "degree")
    print("End Effector at x =", round(p2_x, 1), "y =", round(p2_y, 1))
    base_x = 0
    base_y = 0
    # Plot the links
    #plt.plot([base_x,joint1_x,p2_x],[base_y,jo])
