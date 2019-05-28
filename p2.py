# points: 10

import sys

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import handin2 as nur

def fftIndgen(size):
    """generates indices and amplitudes for fourier transform."""
    
    kx = [x for x in range(-511,513)]
    ky = [y for y in range(-511,513)]

    return kx,ky

def Pk(n,kx,ky):
    # power spec. at kx(0),ky(0) == 0.0
    if kx == 0 and ky == 0:
        return 0.0
    
    P_k = np.sqrt(kx**2 + ky**2)**n

    return P_k

# sample random field, keeping for debugging purposes later
# def gaussian_random_field(Pk):
# 
#     # power spectrum
#     # make my own random numbers here
#     noise = np.fft.fft2(np.random.normal(size = (size,size)))
#     amplitude = np.zeros((size,size))
#     for i, kx in enumerate(fftIndgen(size)):
#         for j, ky in enumerate(fftIndgen(size)):            
#             amplitude[i,j] = Pk2(Pk,kx,ky)
# 
#     return np.fft.ifft2(noise * amplitude)

def main():
    seed = 1239078
    num_pix = 1024
    size = num_pix**2
    kx,ky = fftIndgen(num_pix)
    # amps are 1d
    amps = np.zeros(size)
    n = (-1,-2,-3)
    # need to make my own gaussian dists.
    # my code uses a general 2d so i suppose i'm wasting time but 
    # it returns 2d normal dist so i need a second var. oh well
    x = np.zeros(size)
    y = np.zeros(size)
    z = np.zeros(size)
    xn = np.zeros(size)
    yn = np.zeros(size)
    mu = 0
    sig = 1

    for i in range(len(x)):
        x[i],seed = nur.rng(seed)
        # y[i],seed = nur.rng(seed); leave out for now
        xn[i],yn[i] = nur.normalize_random_distribution(x[i],y[i],mu,sig)

    # begin gauss_field process
    # real & imag are given by gaussian
    for p,k in enumerate(n):
        x2d = x.reshape((num_pix,num_pix))
        gauss_field = np.fft.fft2(x2d)

        for i in range(int(num_pix)):
            for j in range(int(num_pix)):
                amps[j+i*num_pix] = Pk(k,kx[i],ky[j])
        
        # need to reshape to 1d to multiply amplitudes then reshape again
        # with inverse fft
        gauss_field = gauss_field.reshape(-1)
        gauss_field = gauss_field * amps
        gauss_field = np.fft.ifft2(gauss_field.reshape((num_pix,num_pix)))

        plt.figure(figsize=(7,5))
        im = plt.matshow(np.absolute(gauss_field),interpolation='none')
        # ax = plt.gca()
        # plt.colorbar(im,ca)
        plt.xlabel('x [Mpc]',fontsize=20)
        plt.ylabel('y [Mpc]',fontsize=20)
        plt.title('gauss field $n={}$'.format(k),fontsize=25)
        plt.savefig('./plots/gauss_field_n_{}.png'.format(-k),format='png',
                                                            dpi=300)

if __name__ == '__main__':
    sys.exit(main())
