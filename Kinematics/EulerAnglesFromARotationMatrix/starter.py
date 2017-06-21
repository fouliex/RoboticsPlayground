import numpy as np
from sympy.matrices import Matrix
from sympy import symbols, atan2, sqrt

# Conversion Factors

# Fixed Axis X-Y-Z Rotation Matrix
R_XYZ = Matrix([[0.353553390593274, -0.306186217847897, 0.883883476483184],
                [0.353553390593274, 0.918558653543692, 0.176776695296637],
                [-0.866025403784439, 0.25, 0.433012701892219]])

# Conversion Factors
rtd = 180 / np.pi
dtr = np.pi / 180

# Identify useful terms from rotation matrix
r31 = R_XYZ[2, 0]
r11 = R_XYZ[0, 0]
r21 = R_XYZ[1, 0]
r32 = R_XYZ[2, 1]
r33 = R_XYZ[2, 2]

# Euler Angles from Rotation Matrix
# sympy syntax for atan2 is atan2(y, x)
beta = atan2(-r31, sqrt(r11 * r11 + r21 * r21)) * rtd
gamma = atan2(r32, r33) * rtd
alpha = atan2(r21, r11) * rtd

# Calculate the Euler angles that produces a rotation equivalent to R above


print("alpha is = ", alpha, "radians", "or ", alpha * rtd, "degrees")
print("beta  is = ", beta, "radians", "or ", beta * rtd, "degrees")
print("gamma is = ", gamma, "radians", "or ", gamma * rtd, "degrees")
