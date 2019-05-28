# question 1c
# points: 6

import sys

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import handin2 as nur

def main():
    seed = 891238912
    np.random.seed(892378912)
    u = 0
    sigma = 1
    nums = 30
    cdf = nur.gaussian_cdf
    num_samples = np.logspace(1,5,num=nums)
    sample_size = int(1e5)
    my_ks = np.zeros(nums)
    my_prob = np.zeros(nums)
    pyth_ks = np.zeros(nums)
    pyth_prob = np.zeros(nums)

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
        my_ks[i],my_prob[i] = nur.ks_test(x_s,cdf)
        pyth_ks[i],pyth_prob[i] = stats.kstest(x_s,'norm')

        # print('my junk: \n',my_ks[i],my_prob[i])
        # print('stats junk: \n',pyth_ks[i],pyth_prob[i])

    # plotting procedure
    plt.figure(1,figsize=(7,5))
    plt.plot(num_samples,my_ks,c='b',ls='None',marker='.',markersize=1,
            label='my ks test')
    plt.plot(num_samples,pyth_ks,c='r',ls='None',marker='s',markersize=1,
            label='scipy ks test')
    plt.xscale('log')
    plt.xlabel('sample size')
    plt.ylabel('ks statistic')
    plt.legend(frameon=False,loc='best')
    plt.savefig('./plots/ks_stat.png',format='png',dpi=300)

    plt.figure(2,figsize=(7,5))
    plt.plot(num_samples,my_prob,c='b',label='my probabilities')
    plt.plot(num_samples,pyth_prob,c='r',label='scipy probabilities')
    plt.xscale('log')
    plt.xlabel('sample size')
    plt.ylabel('probabilties')
    plt.legend(frameon=False,loc='best')
    plt.savefig('./plots/ks_prob.png',format='png',dpi=300)

if __name__ == '__main__':
    sys.exit(main())
