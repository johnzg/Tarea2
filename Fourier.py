import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq

#guardando datos de las imagenes

seria=plt.imread("cara_02_grisesMF.png")
feliz=plt.imread("cara_03_grisesMF.png")

#implementando la transformada de Fourier en 2D:

def transformadaDeFourier2D(img):
    n=img.shape[0]
    m=img.shape[1]
    l=np.array(range(m))
    res=np.zeros((n,m))    
    for i in range(n):
        for j in range(m):
            for k in range(n):
                aux=np.sum(img[i,:]*(np.exp(1j*2*(np.pi)*(i*(k/n)+l*(j/m)))))
            res[i,j]=aux            
    return res
#print (transformadaDeFourier2D(seria))
print(np.fft.fft2(seria))
