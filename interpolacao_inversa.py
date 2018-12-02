# -*- coding: utf-8 -*-


import numpy as np
from sympy import *
from math import *

from timeit import default_timer as timer

def phix(a, b, c, x0,x): # define função phi(x)

    return a - (b.subs(x,x0)/c.subs(x,x0))

def xProximo(y,Y):

    xR = Y[0,0]

    for i in range(1,Y.shape[1]):

        if(abs(Y[0,i] - y) < abs(xR - y)):
            xR = Y[0,i]
    return xR
    

def newtonRaphson(fx,dfx,x0,e,c,x):

    phi = None
    d = 0

    while (d < c) :

        phi = phix(x0,fx,dfx,x0,x) # calcula phi(x0)

        if(abs(fx.subs(x,x0)) < e): # checa se a função em x0 é menor ou igual à precisão desejada

            return [phi,0,d]

        x0 = phi # caso f(x) não seja perto de 0 o suficiente, x0 recebe o valor de phi(x0) e segue no laço
        
        if(d == c-1):

            return [phi,1]
        
        d+=1


def diferencasDivididas(X,Y):
    if(Y.shape[1] == 1):
        
        return Y[0] 
        
    else:

        X1 = X[:,1:]
        X0 = X[:,:(X.shape[1]-1)]
        Y1 = Y[:,1:]
        Y0 = Y[:,:(Y.shape[1]-1)]

        d = (diferencasDivididas(X1,Y1) - diferencasDivididas(X0,Y0))/(X[X.shape[1]-1] - X[0])
        
        return d         

start = None
end = None

x = symbols('x')

X = Matrix(eval(input("\n\n   Digite o vetor x: ")))
Y = Matrix(eval(input("   Digite o vetor y: ")))

Xp = ones(X.shape[0],X.shape[1])*x - X[:,:]

Pn = zeros(X.shape[0],X.shape[1])

Pn[0,0] = Y[0,0]

Sn = Y[0,0]

start = timer()

for i in range(1,X.shape[1]):
    
    p = 1
    
    for j in range(0,i):
        
        p *= Xp[0,j]
    
    Pn[0,i] = p*diferencasDivididas(X[:,:(i+1)],Y[:,:(i+1)])

end = timer()

for i in range(1,Pn.shape[1]):
    
    Sn += Pn[0,i]

Sn = sympify(Sn)
c = 30
y0 = float(input("   Digite um valor de y para ser testado no polinômio interpolado: "))
e = float(input("   Digite a precisão do x estimado: "))
Sn2 = Sn - y0
print("   Pn(x) = "+str(Sn))
print("   f(xk) = "+str(y0))
print("   xk = "+str(newtonRaphson(Sn2,diff(Sn2,x),xProximo(y0,Y),e,c,x)[0]))
print("   Tempo de execucao total: %e segundos\n\n" % (end - start))
