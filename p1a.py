# question 1a
# points: 4

import sys

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import handin2 as nur

def main():
    # set random seed
    seed = 0
    print(f'seed: {seed}')

    # 1a
    thou = 1000
    mil = 1000000
    x = np.zeros(thou)
    xmil = np.zeros(mil)
    # populating x, xmil (size 1e3, 1e6)
    for i in range(len(x)):
        x[i],seed = nur.rng(seed)

    for i in range(len(xmil)):
        xmil[i],seed = nur.rng(seed)

    # rand_plots(x,xmil)
    # plot of 1000 random numbers x,x_1
    plt.figure(1,figsize=(7,5))
    plt.scatter(x[0:999],x[1:1000],alpha=0.5)
    plt.xlabel('$x_i$',fontsize=14)
    plt.ylabel('$x_{\mathrm{i}+1}$',fontsize=14)
    plt.savefig('./plots/x_x_1.png',format='png',overwrite=True,dpi=300)

    # index x vs val
    plt.figure(2,figsize=(7,5))
    xr = np.arange(0,1000,1)
    plt.xlabel("index of x",fontsize=14)
    plt.ylabel("value of x",fontsize=14)
    plt.scatter(xr,x)
    plt.savefig('./plots/xval_xind.png',format='png',overwrite=True,dpi=300)

    # hist of 1 mil random numbers
    plt.figure(3,figsize=(7,5))
    b = np.linspace(0.0,1.0,20)
    plt.title('1 million random numbers distribution')
    plt.hist(xmil,color='k',bins=b,histtype='step')
    plt.savefig('./plots/1mil_hist.png',format='png',overwrite=True,dpi=300)

if __name__ == "__main__":
    sys.exit(main())

