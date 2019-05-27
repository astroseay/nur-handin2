# problem 6
# points: 10

import sys

import numpy as np
# import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

def dot_prod(x,theta):
    """calculate dot product for minimizing linear regression."""
    
    dotp = np.dot(x,theta)
    return dotp

def predict_min(x,theta,Y):
    dotp = dot_prod(x,theta)
    prediction = ((dotp - Y)**2).mean()/2
    
    return prediction

def abline(x,theta,Y):
    """Plot a line from slope and intercept"""
    
    y_vals = dot_prod(x,theta)
    # plt.xlim(0, 20)
    # plt.ylim(-10, 60)
    plt.xlabel('x [Mpc]')
    plt.ylabel('y [Mpc]')
    plt.gca().set_aspect(0.1, adjustable='datalim')
    plt.plot(x,Y,'.',x, y_vals, '-')
    plt.show()

def gradientDescentLinearRegression(data,alpha=0.047,iter=500000):
    theta0 = []
    theta1 = []
    estimation = []
    predictor = data[1]
    x = np.column_stack((np.ones(len(predictor)),predictor))
    Y = data[4]
    print(predictor,Y)
    theta = np.zeros(2)
    for i in range(iter):
        pred = dot_prod(x,theta)
        t0 = theta[0] - alpha *(pred - Y).mean()
        t1 = theta[1] - alpha *((pred - Y)* x[:,1]).mean()
        
        theta = np.array([t0,t1])
        J = predict_min(x,theta,Y)
        theta0.append(t0)
        theta1.append(t1)
        estimation.append(J)
        if i%1000==0:
            print(f"Iteration: {i+1},Cost = {J},theta = {theta}")
            abline(x,theta,Y)

    print(f'theta0 = {len(theta0)}\ntheta1 = {len(theta1)}\nestimate = {len(estimation)}')

def linear_regression(t90,z_z0):
    """linear regression method test."""

    mean_t90 = np.mean(t90)
    mean_z_z0 = np.mean(z_z0)
    m = len(t90)
    # calculate our constants
    numer = 0
    denom = 0
    for i in range(m):
        numer += (t90[i] - mean_t90) * (z_z0[i] - mean_z_z0)
        denom += (t90[i] - mean_t90)**2
    c1 = numer/denom
    c0 = mean_z_z0 - (c1 * mean_t90)
    print(c1,c0)

    min_x = min(t90)-1
    max_x = max(t90)+1

    xr = np.linspace(min_x,max_x,1000)
    y = c0 + c1*xr

    plt.figure(figsize=(7,5))
    plt.plot(xr,y)
    plt.plot(t90,z_z0,marker='.',ls='None')
    # plt.savefig('p6test.png',format='png',dpi=300)

def plot_features(data):
    """see what features correlate."""

    corr = np.corrcoef(data)
    # for i in range(len(data)):
        # plt.figure(i)
        # plt.plot(data[i],data[1],marker='.',ls='None')
        # plt.savefig('./plots/q6plot_{}.png'.format(i),overwrite=True)
    sns.heatmap(corr,square = True,cbar=True) # ,annot=True,annot_kws={'size': 10})
    plt.savefig('./plots/correlation_map.png',overwrite=True)

def main():
    # z, t90, log(m/m0), sfr, log(z/z0), ssfr, av
    data = np.loadtxt('GRBs.txt',skiprows=2,usecols=(2,3,4,5,6,7,8),unpack=True)
    t90 = data[1]
    z_z0 = data[4]

    # plot_features(data)
    # correlation with t90--log(z/z0) so we'll use data[4] as parameter
    gradientDescentLinearRegression(data)

if __name__ == '__main__':
    sys.exit(main())
