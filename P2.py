import numpy as np
import matplotlib.pyplot as plt

#Punto 1: almacenamiento de datos.
dataInc= np.loadtxt("incompletos.dat", delimiter=",")
dataSig= np.loadtxt("signal.dat", delimiter=",")

#Punto 2: gráfica signal y almacenamiento
xS= np.loadtxt("signal.dat", delimiter=",", usecols=(0,))
yS= np.loadtxt("signal.dat", delimiter=",", usecols=(1,))

xI= np.loadtxt("incompletos.dat", delimiter=",", usecols=(0,))
yI= np.loadtxt("incompletos.dat", delimiter=",", usecols=(1,))

plt.plot(xI,yI)
plt.show()
