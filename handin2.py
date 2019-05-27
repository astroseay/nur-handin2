"""
    @author: christopher seay
        sid: s2286181
        email: seay@strw.leidenuniv.nl
  
    @course: numerical recipes in astrophysics
    @instructor: van daalen, m.p.

"""
import sys

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def rng(seed):
    """generate random number between [0,1).
    uses XOR 64 bit shift, mwc, and mlcg methods
    to generate a pseudorandom number. multiple
    methods are used to minimize correlation.
    args:
        seed: initial seed
    returns:
        I_j: random float [0,1)
        seed: 'new' seed to continue random number generation
    """

    # random int constants to generate random numbers
    a1 = 21
    a2 = 35
    a3 = 4
    a4 = 182937572
    m = 2**64-1
    m2 = 2**32-1
    a = 9824192
    c = 1223536

    # initialize I_j with given seed
    # this seed is newly set after each call
    # start off with a bit of 64-bit XOR-shift
    I_j = seed ^ (seed >> a1)
    I_j = I_j ^ (I_j << a2)
    I_j = I_j ^ (I_j >> a3)

    # mwc
    I_j = a4 * (I_j & m2) + (I_j >> 32)

    # mlcg
    I_j = (a * I_j + c) % m

    seed = I_j # set new "seed" for next iteration

    # convert to float at the end to get numbers b/w 0 and 1
    I_j = np.float64(I_j)/m 

    return I_j, seed

def calc_integral(function,lower_bound,upper_bound,steps):
    """midpoint integrator for improper integrals.
    
    args:
        function: function to be integrated
        lower_bound: lower-bound of integrand
        upper_bound: upper-bound of integrand
        steps: number of romberg splits
    return:
        integrated value
    """

    # shorthand the verbose function input
    fn = function
    a = lower_bound
    b = upper_bound
    h = float(b - a)/steps
    i = 0 # integrand

    for j in range(steps):
        i += fn((a + h / 2.0) + j * h)
    i *= h # final area

    return i

def normalize_random_distribution(u1,u2,mean,stdev):
    """make a normally-distributed set of random numbers.

    using the box-muller methods, generates a normally-distributed set
    of random numbers of arbitrary size, mean, and variance. generates
    x1,x2 but those are separate gaussian distributions. (ie, only one
    is needed for 1d sampling.)

    args:
        u1,u2: random uniform numbers
        mean: desired mean of normal distribution
        variance: desired variance of normal distribution

    returns:
        normally-distributed set of random numbers

    """

    z1 = np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2)
    z2 = np.sqrt(-2*np.log(u1))*np.sin(2*np.pi*u2)
    
    # shifted by sigma and mean
    x1 = mean + z1 * stdev
    x2 = mean + z2 * stdev

    return x1,x2

def error_func(x):
    """error function calculated numerically.
    
    error function errf(x) fits:
        2/sqrt(pi) int exp(-x**2) dx from 0 to x

    args:
        x: upper bound of integrand

    returns:
        error function result

    """
    # for integral
    steps = 1000

    f = lambda x: np.exp(-(x**2))
    errf = 2/np.sqrt(np.pi)*calc_integral(f,0,x,steps)-1

    return errf

def gaussian_cdf(x,mu=0,sigma=1):
    """cumulative distribution function of a gaussian given by wikipedia.

    default mu, sigma is 0, 1. takes any mu,sigma with a drawn sample and computes
    the cdf.

    """

    cdf = 0.5*(1+error_func((x-mu)/(np.sqrt(2)*sigma)))

    return cdf

def ks_test(x,cdf):
    """one-sample kolmogorov-smirnov test.

    nonparametric test goodness of fit test. for the purpose of this function,
    tests goodness of fit between numpy's normal distribution function and 
    the one made from the box-muller algorithm.

    args:
        x: drawn sample
        cdf: cumulative distribution function

    returns:
        goodness of fit maximum distance measure and probability

    """
    
    def prob(z):
        # check if z == 0 to return 1
        if z == 0:
            return 1
        elif z < 1.18:
            v = ((np.exp((-1.*np.pi**2) / (8 * z ** 2))))
            P = (np.sqrt(2*np.pi) / z) * (v + v**9 + v**25)
        else:
            v = np.exp(-2 * z ** 2)
            P = 1 - 2*(v - v**4 + v**9)

        return P

    N = len(x)
    num_bins = int(100*max(x)-min(x))
    counts,bins = np.histogram(x,bins=num_bins)
    width = bins[1]-bins[0]
    bins += width
    dist = np.zeros(len(counts))
    c = sum(counts)
    counts_array = np.zeros(len(counts))

    for i in range(len(counts)):
        dist[i] = abs(sum(counts[:i])/c-cdf(bins[i]))
        counts_array[i] = sum(counts[:i])

    D = max(abs(dist))
    z = D*(np.sqrt(N) + 0.12 + 0.11/np.sqrt(N))
    P = prob(z)

    return D, 1-P
    

def kuiper_test(x,cdf):
    """kuiper test goodness of fit test.

    args:
        x: drawn sample
        cdf: cumulative distribution function

    returns:
        goodness of fit kuiper distance measure and probability
    
    """
    
    def prob(z):
        if z < 0.4:
            return 1
        else:
            v = np.exp(-2*(z**2))
            P = 2 *((4*(z**2-1))*v + (16*z**2-1)*v**4 + (32*z**2-1)*v**9)

        return P

    N = len(x)
    num_bins = int(100*max(x)-min(x))
    counts,bins = np.histogram(x,bins=num_bins)
    width = bins[1]-bins[0]
    bins += width
    dist = np.zeros(len(counts))
    c = sum(counts)
    counts_array = np.zeros(len(counts))

    for i in range(len(counts)):
        dist[i] = abs(sum(counts[:i])/c-cdf(bins[i]))
        counts_array[i] = sum(counts[:i])

    D = abs(max(dist)) + abs(min(dist))
    z = D*(np.sqrt(N) + 0.155 + 0.24/np.sqrt(N))
    P = prob(z)

    return D,P
