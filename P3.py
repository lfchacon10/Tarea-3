from scipy.fftpack import fft, ifft
from matplotlib.image import imread
import numpy as np
import matplotlib.pyplot as plt

#Punto 1: Guarda la imagen.
img = imread('arbol.png')
plt.imshow(img)
plt.show()
#Punto 2: Transformada de Fourier.
imgF = np.fft.fft2(img)
fig= plt.gcf()
plt.imshow(np.abs(imgF))
plt.grid()
plt.savefig("LF.png")
plt.show()

#Punto 3: filtro de la imagen.  
img[np.where(img>3500)] = 0

#Punto 4: log normal.
logCasual = np.log(img_Fourier)
fig= plt.gcf()
plt.imshow(logCasual)
plt.show()


tamano=len(img)
f=500.0
dt=1/(f*32)
freqq=fftpack.fftfreq(tamano,dt)
shiftt=fftpack.fftshift(prft)
ps2D=abs(shiftt)

