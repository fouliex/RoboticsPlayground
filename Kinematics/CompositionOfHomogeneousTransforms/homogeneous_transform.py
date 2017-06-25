from  sympy import symbols , cos, sin , pi , sqrt , simplify
from sympy.matrices import Matrix


# Create symbols for joint variables
# The numbers 1 to 4 correspond to each rotation n the order specified
q1,q2,q3,q4 = symbols('q1:5')

# Define functions for rotation Matrices about x , y and z given specific angle
def rot_x(q):
    R_x =0
    return R_x

def rot_y(q):
    R_y=0
    return R_y

def rot_z(q):
    R_z =0
    return R_z

# Define rotations between frames

# Initial Rotation Matrix for Frame A
Ra = Matrix([[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]])

# Rotations performed on individual Frames for A->B->E
Rb_a =0
Re_b = 0

# Rotations performed on individual Frames for A-C->D->E
Rc_a =0
Rd_c =0
Re_d =0

# Define translations between  frames
tb_a =0
te_b =0
tc_a =0
td_c =0
te_d =0

# Define homogeneous transformation matrices
tb_a =0
te_b =0
tc_a =0
td_c =0
te_d =0

# Composition of Transformations
