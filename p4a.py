# question 4a
# points: 6

import sys

import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import handin2 as nur

def main():
    # calculated by hand, terms in front of integral
    H_z50 = 13964.33333 # km/s/Mpc
    c = 2675 # units of H_0**2
    omega_m = 0.3
    omega_dm = 0.7
    H_0 = 70 # km/s/Mpc
    lo_z = 50
    up_z = int(1e4) # something large that's not np.inf
    # integrand defined for function f
    f = lambda z: (1+z) / (H_0**3 * (omega_m*(1+z)**3 + omega_dm))**(1.5)
    steps = 10000 

    integral = nur.calc_integral(f,lo_z,up_z,steps)
    py_int = quad(f,lo_z,np.inf)
    res = integral*c*H_z50
    err = (integral-py_int[0])/py_int[0]
    print('integral: {}\nreal: {}\naccuracy: {}\ngrowth factor: {}\n \
            python acc: {}'.format(integral,py_int[0],err,res,py_int[1]))
    
    # sample to check integrand
    # fx = lambda x: np.exp(-x**2)
    # lb = -1
    # ub = 1
    # s = 1000
    # print(nur.calc_integral(fx,lb,ub,s))

if __name__ == '__main__':
    sys.exit(main())
