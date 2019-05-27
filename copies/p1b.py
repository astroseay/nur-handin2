# question 1b
# points: 4

import sys
 
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import handin2 as nur


def main():
    seed = 12784
    u = 3 # mean
    sigma = 2.4 # standard deviation
    thou = 1000
    x1 = np.zeros(thou)
    x2 = np.zeros(thou)
    x1_norm = np.zeros(thou)
    x2_norm = np.zeros(thou)
    true_gauss = np.random.normal(loc=u,scale=sigma,size=thou) # for comp
    for i in range(len(x1)):
        # populate uniform random numbers then make gaussian
        x1[i],seed = nur.rng(seed)
        x2[i],seed = nur.rng(seed)
        x1_norm[i],x2_norm[i] = nur.normalize_random_distribution(
                x1[i],
                x2[i],
                u,
                sigma)

    # plotting procedure
    # compare with scipy
    x = np.linspace(u - 5*sigma,u + 5*sigma,1000)
    plt.figure(1)
    plt.hist(x1_norm,density=True,bins=50)
    plt.plot(x,stats.norm.pdf(x,u,sigma))
    plt.axvline(x=u + sigma, c='r')
    plt.axvline(x=u - sigma, c='r')
    plt.axvline(x=u - 2 * sigma, c='k')
    plt.axvline(x=u - 3 * sigma, c='k')
    plt.axvline(x=u - 4 * sigma, c='k')
    plt.axvline(x=u + 2 * sigma, c='k')
    plt.axvline(x=u + 3 * sigma, c='k')
    plt.axvline(x=u + 4 * sigma, c='k')
    plt.xlim(u - 5 * sigma, u + 5 * sigma)
    plt.savefig("./plots/box_gauss.png",overwrite=True,dpi=300)

if __name__ == '__main__':
    sys.exit(main())
