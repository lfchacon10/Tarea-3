#PYTHON3
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

#Punto 1: almacenamiento de datos.
dataInc= np.loadtxt("incompletos.dat", delimiter=",")
dataSig= np.loadtxt("signal.dat", delimiter=",")

#Punto 2: gráfica signal y almacenamiento
xS= np.loadtxt("signal.dat", delimiter=",", usecols=(0,))
yS= np.loadtxt("signal.dat", delimiter=",", usecols=(1,))

xI= np.loadtxt("incompletos.dat", delimiter=",", usecols=(0,))
yI= np.loadtxt("incompletos.dat", delimiter=",", usecols=(1,))

plt.plot(xS,yS)
plt.title("Data from Signal")
plt.grid()
plt.savefig("ChaconLuis_signal.pdf")
plt.show()

#Punto 3: gráfica de la transformada de Fourier de los datos d la señal.

print(len(xS))
n = 512 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 50 ) #50 samples per unit frequency
t = np.linspace( 0, (n-1)*dt, n)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )

fft_x = fft(y) / n # FFT Normalized
freq = fftfreq(n, dt) # Recuperamos las frecuencias

plt.plot(freq,abs(fft_x))
plt.title("Fourier transform")
plt.grid()
plt.savefig('ChaconLuis_TF.png')
plt.show()
