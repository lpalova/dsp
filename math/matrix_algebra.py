# Matrix Algebra
import numpy as np
from numpy import linalg as LA

a = np.array([[1, 2, 3], [2, 7, 4]])
b = np.array([[1, -1], [0, 1]])
c = np.array([[5, -1], [9, 1], [6,0]])
d = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([[6, 2, -3, 5]])
v = np.array([[3, 5, -1, 4]])
w = np.array([[1], [8], [0], [5]])

#Q1
a.shape
#(2, 3)
b.shape
# (2,2)
c.shape
# (3,2)
d.shape
# (2,3)
u.shape
# (1,4)
w.shape
# (4,1)

#Q2
np.add(u,v)
#array([[ 9,  7, -4,  9]])
np.subtract(u,v)
#array([[ 3, -3, -2,  1]])
np.multiply(6,u)
#array([[ 36,  12, -18,  30]])
np.vdot(u,v)
#51
LA.norm(u)
#8.6023252670426267

#Q3
np.add(a,c)
#not defined
np.subtract(a,np.transpose(c))
#array([[-4, -7, -3],
#       [ 3,  6,  4]])
np.add(np.transpose(c),np.multiply(3,d))
#array([[ 14,   3,   3],
#       [  2,   7,   9]])
np.dot(b,a)
#array([[-1, -5, -1],
#       [ 2,  7,  4]])
np.dot(b,np.transpose(a))
#not defined
np.dot(b,c)
#not defined
np.dot(c,b)
#array([[ 5, -6],
#       [ 9, -8],
#       [ 6, -6]])
LA.matrix_power(b,4)
#array([[ 1, -4],
#       [ 0,  1]])
np.dot(a,np.transpose(a))
#array([[14, 28],
#       [28, 69]])
np.dot(np.transpose(d),d)
#array([[10, -4,  0],
#       [-4,  8,  8],
#       [ 0,  8, 10]])
