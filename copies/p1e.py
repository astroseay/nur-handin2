# question 1e
# points: 6
# not started yet!!

import sys

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import handin2 as nur

def main():
    seed = 4
    np.random.seed(4)
    u = 0
    sigma = 1
    data = np.loadtxt('randomnumbers.txt',unpack=True)
    # number of random nums, number of sets
    dsize = len(data[0,:])
    dsets = len(data[:,0]) 
    sample_size = int(np.log10(dsize))
    num_samples = np.logspace(1,sample_size,num=10)
    print(num_samples)

    # random number params
    x = np.zeros(sample_size)
    y = np.zeros(sample_size)
    xn = np.zeros(sample_size)
    yn = np.zeros(sample_size)

    # want to generate one sample of appropriate size then take slices
    for i in range(sample_size):
        x[i],seed = nur.rng(seed)
        xn[i],yn[i] = nur.normalize_random_distribution(x[i],y[i],u,sigma)

    # finish later

if __name__  == '__main__':
    sys.exit(main())
