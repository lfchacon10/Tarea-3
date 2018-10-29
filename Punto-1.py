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


#Commit terminal
