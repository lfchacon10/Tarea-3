from scipy import fftpack
import numpy as np


#Punto 1: Guarda la imagen.
img = plt.imread('arbol.png')

tamano=len(img)
f=500.0
dt=1/(f*32)

img_fourier=fftpack.fft2(img)
plt.imshow(abs(img_fourier))
plt.show()


freqq=fftpack.fftfreq(tamano,dt)
shiftt=fftpack.fftshift(prft)
ps2D=abs(shiftt)

