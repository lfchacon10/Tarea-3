from scipy import fftpack

#Punto 1: Guarda la imagen.
img = plt.imread('arbol.png')

tamano=len(img)
f=500.0
dt=1/(f*32)

prft=fftpack.fft2(img)
freqq=fftpack.fftfreq(tamano,dt)
shiftt=fftpack.fftshift(prft)
ps2D=abs(shiftt)

