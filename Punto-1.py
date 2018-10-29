import numpy as np
import matplotlib.pyplot as plt
import wget



#Punto 1: almacenar datos.
url = "http://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/WDBC.dat"
datos = wget.download(url, "./DatosCancer.txt") 
misdatos = np.genfromtxt ("DatosCancer.txt")

#Lectura de datos

with open ("DatosCancer.txt") as F:
    c = F.readlines()

matriz=[]

for i in range(len(c)):
    linea = c[i]
    linea=linea.split(",")
    matriz.append(linea)
matriz=np.array(matriz).T
print(matriz)

#Covierte toda la matriz a floats. Para valores Benignos = 1 y Malignos =1

for i in range ( len(matriz[:])):
    for j in range (len (matriz[:][0]) ):
        if( i == 1):
            if( matriz[i][j] == 'M'):
                matriz[i][j] = 0
            else: matriz[i][j] = 1
        matriz[i][j] = float(matriz[i][j])


