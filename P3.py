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
plt.savefig("ChaconLuis_FT2D.pdf")


#Punto 3: filtro de la imagen.  
freqq = fftpack.fftfreq(tamano, dt)
shiftt= fftpack.fftshift(imgF)
ps = abs(shiftt)
plt.imshow(imgF.real**2 + imgF.imag**2)

freq_cut = 3500.0
imgF[abs(freqq)>freq_cut] = 0
logNormal = np.log(abs(imgF))
plt.imshow(logNormal)
plt.show()


imgFinal= fftpack.ifft2(imgF).real
plt.imshow(imgFinal, cmap="gray")
plt.show()


cleanf=np.fft.ifft2(img,axes=(0, 1))
cleanr=cleanf.real
plt.figure(figsize=(10,10))
plt.imshow(cleanr)
plt.show()
#Punto 4: log normal.


