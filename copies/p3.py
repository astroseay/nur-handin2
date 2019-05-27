# question 3
# points: 8

import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def a(t,H_0):
    """scale factor function."""

    return (1.5*H_0*t)**(2/3)

def a_dot(t,H_0):
    """da/dt equation."""
    
    return (H_0*(1/5*H_0*t)**(-1/3))

def ODE_solver(E,t,H_0,omega_0):
    """2nd order ODE simplified to 1st order.

    specific solver for 2nd order ODE. because rk4 is for 1st order ODEs only
    
    args:
        E: linearized dD/dt
        t: timestep

    returns:
        solved ode for timestep

    """

    init_D = E[0]
    dD_dt = E[1]
    # terms for d2D_dt2
    first_term = -2 * (a_dot(t,H_0) / a(t,H_0)) * (dD_dt)
    sec_term = 1.5*omega_0*H_0**2*a(t,H_0)**(-3)*init_D
    d2D_dt2 = first_term + sec_term
    ode = np.array([dD_dt,d2D_dt2])
    
    return ode

def rk4(ODE_solver,E,t,h,H_0,omega_0):
    """runge-kutta 4th order ode solver algorithm.

    args:
        f: ODE_solver
        E: dD/dt
        t: time to solve for
        h: step size

    returns:
        solution to ode

    """
    # functions f,g -> f(t,D,E), g(t,D,E)
    f = ODE_solver
    k1 = h*f(E,t,H_0,omega_0)
    k2 = h*f(E + k1/2, t + h/2,H_0,omega_0)
    k3 = h*f(E + k2/2, t + h/2,H_0,omega_0)
    k4 = h*f(E + k3, t + h,H_0,omega_0)
    soln = k1/6 + k2/3 + k3/3 + k4/6

    return soln

def ODE_to_solve(case,start,end,size,H_0,omega_0):
    """solves the ODE step-by-step.

    args:
        case: initial conditions
        start: start condition
        end: end condition
        size: number of points between start and end

    returns:
        solution to ODE

    """

    # integration step-size
    step = (end-start)/size

    # initial conditions
    E = case
    times = np.arange(start,end,step)
    D = np.zeros(size)
    
    # now call runge-kutta solver
    for i in range(len(times)):
        D[i] = E[0]
        E += rk4(ODE_solver,E,times[i],step,H_0,omega_0)

    return times,D

def main():
    H_0 = 7.16e-11 # yr-1 or 70.0 km/s/Mpc
    omega_0 = 1 # E-dS universe
    delta_t = 10 # yrs
    t_start = 1 # yrs
    t_end = 1000 # yrs
    time_steps = int((t_end - t_start) / delta_t) # num. of time steps
    cases = ([3,2],[10,-10],[5,0])
    labels = ('D(1)=3, D\'(1)=2','D(1)=10, D\'(1)=-10','D(1)=5, D\'(1)=0')

    for i in range(len(cases)):
        t,D = ODE_to_solve(cases[i],t_start,t_end,time_steps,H_0,omega_0)
        plt.loglog(t,D,label=labels[i])

    plt.xlabel('t [yr]')
    plt.ylabel('D(t)')
    plt.legend(loc='best',frameon=False)
    plt.savefig('./plots/rk4.png',format='png',dpi=300)

if __name__ == '__main__':
    sys.exit(main())
