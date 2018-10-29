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


#Covarianza
def covarianza (x,y):
	for i in range(len(x)):
		for j in range(len(y)):
			sumaCova= (x[i]-np.mean(x))*(y[j]- np.mean(y))
	return sumaCova/ len(x)

#Matriz covarianza. No vamos a tener en cuenta la variable ID ya que no tiene nada ver con tener cancer. Se dejara la variable Diagnosis para poder ver que variable es la que mas influye en esta diagnosis.

cantidadVariables = len(matriz[:])
matrizCova= np.zeros((cantidadVariables, cantidadVariables) )
for i in range (cantidadVariables):
    for j in range (cantidadVariables):
        if( i == 32):
            matrizCova[i][j] = covarianza( matriz[i], matriz[i])
        else: matrizCova[i][j] = covarianza( matriz[i], matriz[j])

print ("MIA ", matrizCova, " CALCULADO POR NP ",np.cov(matriz) )


#Punto 3: calcula autovalores y autovectores.

eigenValues = np.eig( matrizCova)
eigenVectors = np.eig( matrizCova)

#for i in range (len (eigenValues)):
#	print ( "ID EigenValue: "eigenValues[i], "ID EigenVector: ", eigenVectors[i], "\n Radius EigenValue: ", eigenValues[i],  " Radius EigenVector: ",eigenVectors[i], "\n Texture EigenValue: ", eigenValues[i],  " Texture EigenVector: ",eigenVectors[i], "\n Perimeter EigenValue: ", eigenValues[i],  " Perimeter EigenVector: ",eigenVectors[i], "\n Area EigenValue: ", eigenValues[i],  " Area EigenVector: ",eigenVectors[i], "\n Smoothness EigenValue: ", eigenValues[i],  " Smoothness EigenVector: ",eigenVectors[i], "\n Compactness EigenValue: ", eigenValues[i],  " Compactness EigenVector: ",eigenVectors[i], "\n Concavity EigenValue: ", eigenValues[i],  " Concavity EigenVector: ",eigenVectors[i], "\n Concave EigenValue: ", eigenValues[i],  " Concave EigenVector: ",eigenVectors[i], "\n Symmetry EigenValue: ", eigenValues[i],  " Symmetry EigenVector: ",eigenVectors[i],  "\n Fractal dimension EigenValue: ", eigenValues[i],  " Fractal dimension EigenVector: ",eigenVectors[i] )



