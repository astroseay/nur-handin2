import sys

import numpy as np
# import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def make_grid(size=16):
    """make a 16**3 grid with cell width 1."""

    X = np.zeros(size)
    Y = np.zeros(size)
    Z = np.zeros(size)
    grid = np.zeros((size,size,size))
    for i in range(size):
        for j in range(size):
            for k in range(size):
                grid[i][j][k] = k
    
    return grid

def assign_mass(xp,yp,zp,grid):
    """assign masses using nearest neighbor method."""
    
    masses = np.zeros(shape=(16,16,16))
    for x,y,z in list(zip(xp,yp,zp)):
        # finds places to assign mass based off of position
        x_min = np.argmin(abs(x - grid[:,0]))
        y_min = np.argmin(abs(y - grid[:,1]))
        z_min = np.argmin(abs(z - grid[:,2]))
        # masses[grid[x_min][0][0]][grid[1][y_min][1][grid[2][2][z_min]] += 1

    return masses

def main():
    np.random.seed(121)
    positions = np.random.uniform(low=0,high=16,size=(3,1024))
    x,y,z = positions[0],positions[1],positions[2]
    grid = make_grid()
    grid_masses = assign_mass(x,y,z,grid)

    # fig = plt.figure()
    ax = plt.axes(projection='3d')    
    ax.scatter(x,y,z,c=z,cmap='magma',lw=0.5)
    # plt.show()
    plt.savefig('q5atest.png',format='png',dpi=300)

if __name__ == '__main__':
    sys.exit(main())
