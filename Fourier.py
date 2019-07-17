import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq

#guardando datos de las imagenes

seria=plt.imread("cara_02_grisesMF.png")
feliz=plt.imread("cara_03_grisesMF.png")

#sacando la trasnformada de fourier y ordenandola
transSeria=np.fft.fft2(seria)
transFeliz=np.fft.fft2(feliz)

transSeriaOrdenada=np.fft.fftshift(transSeria)
transFelizOrdenada=np.fft.fftshift(transFeliz)

#Graficando los espectros de la trasnformada de fourier de las dos imagenes
plt.figure()

plt.subplot(1,2,1)
plt.imshow(transSeriaOrdenada.real,vmin=-70,vmax=70)
plt.title("Espectro Fourier Seria")

plt.subplot(1,2,2)
plt.imshow(transFelizOrdenada.real,vmin=-70,vmax=70)
plt.title("Espectro Fourier Feliz")

plt.savefig("espectroFourierImagenes.png")

#filtrando espectro de Fourier de las imagenes
aux=np.zeros((254,170),dtype=bool)
for i in range(254):
    for j in range(170):
        if(abs(transSeria[i,j]) < 24.0 ):
            aux[i,j]=True
transSeriaFiltrada=np.where(aux ,transSeria,0)

aux=np.zeros((254,170),dtype=bool)
for i in range(254):
    for j in range(170):
        if(abs(transFeliz[i,j]) > 16.0 ):
            aux[i,j]=True          
transFelizFiltrada=np.where(aux ,transFeliz,0)

#Recuperando las imagenes filtradas a traves de la trasformada de Fourier inversa
seriaFiltrada=np.fft.ifft2(transSeriaFiltrada)
felizFiltrada=np.fft.ifft2(transFelizFiltrada)


#Graficando las imagenes recuperadas

plt.figure()

plt.subplot(1,2,1)
plt.axis('off')
plt.imshow(-seriaFiltrada.real,cmap='Greys')
plt.title("Seria Filtrada")

plt.subplot(1,2,2)
plt.axis('off')
plt.imshow(-felizFiltrada.real,cmap='Greys')
plt.title("Feliz Filtrada")

plt.savefig("imagenesFiltradas.png")

#Creando la imagen hibrida a partir de las imagenes filtradas anteriormente

transHibrida=2.5*transSeriaFiltrada+0.7*transFelizFiltrada

#Recuperando la imagen hibrida usando la transformada de Fourier inversa

hibrida=np.fft.ifft2(transHibrida)

#Graficando la imagen hibrida 

plt.figure()
plt.axis('off')
plt.imshow(-hibrida.real,cmap='Greys')
plt.title("Imagen Hibrida")
plt.savefig("Hibrida.png")