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

#Cree una funcion para Sumar y para dar el mean ya que con NP por algún extraño motivo no me funciono. Es posible que sea por los ' ' que prevalecene n el archivo incluso despues de convertir la matriz a float.
def SumYMean( x ):
    sum =0
    for i in range(len(x)):
        sum+= float(x[i])
    mean = sum / len(x)
    return sum, mean



