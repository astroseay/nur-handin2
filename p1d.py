# question 1d
# points: 6

import sys

import numpy as np
from astropy.stats import kuiper
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import handin2 as nur

def main():
    seed = 8912312
    np.random.seed(8912312)
    u = 0
    sigma = 1
    cdf = nur.gaussian_cdf
    num_samples = np.logspace(1,5,num=50)
    sample_size = int(1e5)
    my_k = np.zeros(50)
    my_p = np.zeros(50)
    pyth_k = np.zeros(50)
    pyth_p = np.zeros(50)

    # random number params
    x = np.zeros(sample_size)
    y = np.zeros(sample_size)
    xn = np.zeros(sample_size)
    yn = np.zeros(sample_size)

    # want to generate one sample of 1e5 numbers then take slices
    for i in range(sample_size):
        x[i],seed = nur.rng(seed)
        xn[i],yn[i] = nur.normalize_random_distribution(x[i],y[i],u,sigma)

    for i,s in enumerate(num_samples):
        # slice of x at given s
        x_s = xn[:int(s)]
        x_k = x[:int(s)]
        my_k[i],my_p[i] = nur.kuiper_test(x_s,cdf)
        pyth_k[i],pyth_p[i] = kuiper(x_k)

    # plotting procedure
    plt.figure(1,figsize=(7,5))
    plt.plot(num_samples,my_k,c='b',ls='None',marker='.',markersize=1,
            label='my kuiper test')
    plt.plot(num_samples,pyth_k,c='r',ls='None',marker='s',markersize=1,
            label='astropy kuiper test')
    plt.xscale('log')
    plt.xlabel("number of points")
    plt.ylabel("kuiper statistic")
    plt.legend()
    plt.savefig('./plots/kuiper_stat.png',format='png',dpi=300)

    plt.figure(2,figsize=(7,5))
    plt.plot(num_samples,my_p,c='b',label='my probabilities')
    plt.plot(num_samples,pyth_p,c='r',label='astropy probabilities')
    plt.xscale('log')
    plt.xlabel('sample size')
    plt.ylabel('probabilties')
    plt.legend(frameon=False,loc='best')
    plt.savefig('./plots/k_prob.png',format='png',dpi=300)

if __name__ == '__main__':
    sys.exit(main())
