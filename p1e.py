# question 1e
# points: 6

import sys

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import handin2 as nur

def cdf(x,s):

    """cdf of sample drawn and random sample from input txt.

    args:
        x: my sample
        s: sample from input data

    returns:
        function cdf to find ks statistic and probabilities

    """
    
    # find where s < x and the cdf is that over the length of s.
    n = len(s)
    d = s < x
    y = len(d)

    return d/n

def main():
    seed = 4
    np.random.seed(4)
    u = 0
    sigma = 1
    data = np.loadtxt('randomnumbers.txt',unpack=True)
    # number of random nums, number of sets
    dsize = len(data[0,:])
    dsets = len(data[:,0])
    # print(dsize,dsets)
    sample_size = int(np.log10(dsize))
    num_samples = np.logspace(1,sample_size,num=30)
    # print(num_samples)
    ks_stat = np.zeros(30)
    prob = np.zeros(30)

    # random number params
    x = np.zeros(sample_size)
    y = np.zeros(sample_size)
    xn = np.zeros(sample_size)
    yn = np.zeros(sample_size)

    # want to generate one sample of appropriate size then take slices
    for i in range(sample_size):
        x[i],seed = nur.rng(seed)
        xn[i],yn[i] = nur.normalize_random_distribution(x[i],y[i],u,sigma)

    # none of this will work, explain in report
    for i in range(dsets):
        for j,s in enumerate(num_samples):
            x_s = xn[:int(s)]
            d_s = data[:dsize,i]
            # need a 2d ks test
            # ks_stat[i],prob[i] = nur.ks_test(x_s,d_s)

if __name__  == '__main__':
    sys.exit(main())
