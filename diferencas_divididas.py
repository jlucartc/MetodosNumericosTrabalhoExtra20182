import numpy as np
from sympy import *
from math import *


def diferencasDivididas(X,Y):
    if(Y.shape[1] == 1):

        #print(Y[0])
        return Y[0] 
        
    else:

        X1 = X[:,1:]
        X0 = X[:,:(X.shape[1]-1)]
        Y1 = Y[:,1:]
        Y0 = Y[:,:(Y.shape[1]-1)]

        d = (diferencasDivididas(X1,Y1) - diferencasDivididas(X0,Y0))/(X[X.shape[1]-1] - X[0])

        print("X0: ",X0)
        print("X1: ",X1)
        print("Y0: ",Y0)
        print("Y1: ",Y1)

        print("d: ",d)

        return d         

x = symbols('x')

X = Matrix(eval(input("Digite o vetor x: ")))
Y = Matrix(eval(input("Digite o vetor y: ")))

print(diferencasDivididas(X,Y))

