from scipy import fftpack
from matplotlib.image import imread
import numpy as np
import matplotlib.pyplot as plt

#Punto 1: Guarda la imagen.
img = imread("arbol.png")
tamano=len(img)
f=500.0
dt=1/(f*32)

#Punto 2: Transformada de Fourier.
imgF = fftpack.fft2(img, shape= img.shape[:2],axes=(0,1))
plt.figure()
fig= plt.gcf()
plt.plot( abs(imgF) )
fig.savefig("ChaconLuis_FT2D.pdf")


#Punto 3: filtro de la imagen.Mejor intento
freq_cut = 4000
imgF[abs(imgF)>freq_cut] = 0
logNormal = np.log(abs(imgF))
plt.figure()
fig= plt.gcf()
plt.imshow(logNormal)
fig.savefig("ChaconLuis_FT2D_filtrada.pdf")

#Punto 4: Imagen filtrada.
imgFinal= fftpack.ifft2(imgF).real
plt.figure()
fig= plt.gcf()
plt.imshow(imgFinal, cmap="gray")
fig.savefig("ChaconLuis_Imagen_filtrada.pdf")




