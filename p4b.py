# question 4b
# points: 2

import sys

import numpy as np

import handin2 as nur

def main():
    lo_a = 0
    up_a = 1 / 51 # z = 50, a = 1/(1+z)
    steps = 10000
    omega_m = 0.3
    omega_dm = 0.7
    H_0 = 70
    f = lambda a: (1/a**3) / (omega_m/a**3 + omega_dm)**(1.5)
    integral = nur.calc_integral(f,lo_a,up_a,steps)
    print('integral: {}'.format(integral))
    analytic_deriv = (-15/4)*(omega_m**2)*H_0 * (integral/(up_a)**3)
    print('analytic d/dz of lgf at z = 50: {}'.format(analytic_deriv))

if __name__ == '__main__':
    sys.exit(main())
