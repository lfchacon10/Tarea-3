from scipy import fftpack
import numpy as np


#Punto 1: Guarda la imagen.
img = plt.imread('arbol.png')

tamano=len(img)
f=500.0
dt=1/(f*32)

#Punto 2: Transformada de Fourier.
img_fourier=fftpack.fft2(img)
plt.imshow(abs(img_fourier))
plt.show()

#Punto 3: filtro de la imagen.  
img[where(img>3500)] = 0


freqq=fftpack.fftfreq(tamano,dt)
shiftt=fftpack.fftshift(prft)
ps2D=abs(shiftt)

