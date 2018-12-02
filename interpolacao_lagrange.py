# -*- coding:utf-8 -*-

import numpy as np
from sympy import *
from math import *

from timeit import default_timer as timer

def lagrange(X,Y,x):
    Z = zeros(X.shape[0],X.shape[1])
    Pn = Z[:,:]
    n = 1
    d = 1
    Mxk = Z[:,:]
    for i in range(0,X.shape[1]):
        Pn[0,i] = 0
        n = 1
        d = 1
        for j in range(0,X.shape[1]):    
            if(j != i):
                n *= x - X[0,j]
                d *= X[0,i] - X[0,j]
        Pn[0,i] = Y[0,i]*(n/d)
    return Pn

start = None
end = None

x = symbols('x')

X = Matrix(eval(input("\n\n   Digite os valores de x -> [[x0,x1,{...},xn]]: ")))
Y = Matrix(eval(input("   Digite os valores de y -> [[y0,y1,{...},yn]]: ")))

start = timer()

L = lagrange(X,Y,x)

end = timer()

LM = 0

for i in range(0,L.shape[1]):
    
    LM += L[0,i]
    
    
LM = sympify(LM)

x0 = float(input("   Digite um valor de x para ser testado no polinômio interpolado: "))
print("   y(x) = "+str(LM))
print("   y("+str(x0)+") = "+str(LM.subs(x,x0)))
print("   Tempo de execucao total: %e segundos\n\n" % (end - start))
