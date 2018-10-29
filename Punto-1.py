import numpy as np
import matplotlib.pyplot as plt
import wget



#Punto 1: almacenar datos.
url = "http://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/WDBC.dat"
#datos = wget.download(url, "./DatosCancer.txt") 
misdatos = np.genfromtxt ("DatosCancer.txt")

#Lectura de datos

with open ("DatosCancer.txt") as F:
    c = F.readlines()

matriz=[]

def lineToNumbers(l):
	l = l.split(",")
	nL=np.zeros((len(l)))
	for i in range(len(l)):
		if( l[i] == 'M'):
			nL[i]=0.0
		elif( l[i] == 'B'): nL[i] =1.0
		else:	nL[i] = float(l[i])
	return nL

for i in range(len(c)):
    linea = c[i]
    nLinea = lineToNumbers(linea)
    matriz.append(nLinea)

matriz=np.array(matriz).T

print (matriz)

#Cree una funcion para Sumar y para dar el mean ya que con NP por algún extraño motivo no me funciono. Es posible que sea por los ' ' que prevalecene n el archivo incluso despues de convertir la matriz a float.
def sumYMean( x ):
    sum =0
    for i in range(len(x)):
        sum+= float(x[i])
    mean = sum / len(x)
    return sum, mean

#Covarianza

def covarianza (x,y):
    sumX, meanX = sumYMean(x)
    sumY, meanY = sumYMean(y)
    for i in range(len(x)):
        for j in range(len(y)):
            sumaCova= (float(x[i])-meanX)*(float(y[j])- meanY)
    return sumaCova/ len(x)


#Matriz covarianza. No vamos a tener en cuenta la variable ID ya que no tiene nada ver con tener cancer. Se dejara la variable Diagnosis para poder ver que variable es la que mas influye en esta diagnosis.

cantidadVariables = len(matriz[:]) -1
matrizCova= np.zeros((cantidadVariables, cantidadVariables) )
for i in range (cantidadVariables):
    for j in range (cantidadVariables):
        if( i == 31):
            matrizCova[i][j] = covarianza( matriz[i+1], matriz[i+1])
        else: matrizCova[i][j] = covarianza( matriz[i+1], matriz[j+1])





