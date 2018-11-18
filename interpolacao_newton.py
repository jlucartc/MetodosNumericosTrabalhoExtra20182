import numpy as np
from sympy import *
from math import *

from timeit import default_timer as timer

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

X = Matrix(eval(input("Digite o vetor x: ")))
Y = Matrix(eval(input("Digite o vetor y: ")))

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
    
x0 = float(input("Digite um valor de x para ser testado no polinômio interpolado: "))
print("y(x) = ",str(Sn))
print("y("+str(x0)+") = ",Sn.subs(x,x0))
print("Tempo de execucao total: %e segundos" % (end - start))
