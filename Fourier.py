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
            aux=0.0
            for k in range(n):
                aux+=np.sum(img[i,:]*(np.exp(1j*2*(np.pi)*(i*(k/n)+l*(j/m)))))
            res[i,j]=aux            
    return res
#print (transformadaDeFourier2D(seria))
print(np.fft.fft2(seria))

transSeria=np.fft.fft2(seria)
transFeliz=np.fft.fft2(feliz)

#sinValoresGrandes=np.where(np.abs(transImg)<30, transImg, 30 )

transSeriaOrdenada=np.fft.fftshift(transSeria)
transFelizOrdenada=np.fft.fftshift(transFeliz)

#Graficando los espectros de la trasnformada de fourier de las dos imagenes
plt.figure()
plt.imshow(transSeriaOrdenada.real)
plt.savefig("espectroFourierImagenSeria.png")

plt.figure()
plt.imshow(transFelizOrdenada.real)
plt.savefig("espectroFourierImagenFeliz.png")

#extrayendo la informacion deseada de las imagenes
aux=np.zeros((254,170),dtype=bool)
for i in range(254):
    for j in range(170):
        if(transImg[i,j] < 4000 ):
            aux[i,j]=True
infoSeria=np.where(aux ,transImg,0)

