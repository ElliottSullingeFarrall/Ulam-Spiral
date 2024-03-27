from numpy import array, arange, fromfunction, flip, zeros, vectorize, exp
from sympy import isprime, primerange
import matplotlib.pyplot as plt

import sys

def ulam_square(n):
    if n == 0:
        square = array([[1]])
    else:
        o = 2*n + 1

        b = arange(o**2 - 1*o + 1, o**2 - 0*o + 1)
        l = arange(o**2 - 2*o + 2, o**2 - 1*o + 2)
        t = arange(o**2 - 3*o + 3, o**2 - 2*o + 3)
        r = arange(o**2 - 4*o + 4, o**2 - 3*o + 4)

        square = zeros((o, o), dtype=int)
        square[:, o-1]  = flip(r)
        square[0, :]    = flip(t)
        square[:, 0]    = l
        square[o-1, :]  = b

        square[1:o-1, 1:o-1] = ulam_square(n-1)
    return square

GRID_SIZE = 250
sys.setrecursionlimit(GRID_SIZE + 3)

Z = vectorize(isprime)(ulam_square(GRID_SIZE))

fig, ax = plt.subplots()
ax.axis('off')
ax.imshow(Z, cmap='gray')
fig.savefig('ulam.png', bbox_inches='tight', pad_inches=0)

# --------------------------------- Extension -------------------------------- #

N = 10_000

pts = fromfunction(lambda n: n*exp(n*1j), (N,))
pts = pts[list(primerange(N))]

fig, ax = plt.subplots()
ax.axis('off')
plt.scatter(pts.real, pts.imag, s=1, c='black')
fig.savefig('polar.png')