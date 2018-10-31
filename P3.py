from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt

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
img[np.where(img>3500)] = 0

#Punto 4: log normal.
logCasual = log(img_Fourier)
plt.imshow(logCasual)
plt.show()

freqq=fftpack.fftfreq(tamano,dt)
shiftt=fftpack.fftshift(prft)
ps2D=abs(shiftt)

