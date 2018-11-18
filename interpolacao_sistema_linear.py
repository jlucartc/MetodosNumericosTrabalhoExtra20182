import numpy as np
from sympy import *
from math import *

from timeit import default_timer as timer

def resolveTriangular(A):

    R = np.asmatrix([0]*A.shape[0]) # matriz de valores das icógnitas
    R = R.astype(float)

    for i in range(A.shape[0]-1,-1,-1):

        R[0,i] = np.copy(R[0,i]) + np.copy(A[i,A.shape[0]])

        for j in range(A.shape[0]-1,i,-1):

            R[0,i] = np.copy(R[0,i]) - np.copy(A[i,j])

        R[0,i] = (np.copy(R[0,i])/np.copy(A[i,i]))

        A[:,i] = np.copy(A[:,i])*np.copy(R[0,i])


    return [A,R]

def pivotacaoParcial(A):

    p = 0
    m = None

    for i in range(0,A.shape[0]):
        for j in range(i+1,A.shape[0]):
            if A[i,i] < A[j,i]:
                p += 1
                Temp = np.copy(A[i])
                A[i] = np.copy(A[j])
                A[j] = np.copy(Temp)
                
        for k in range(i+1,A.shape[0]):
            d = np.copy(A[k,i])
            d = d/np.copy(A[i,i])
            A[k,:] = np.copy(A[k,:]) - (np.copy(A[i,:])*d)
                
    return [A,p]

start = None
end = None    

x = np.matrix(eval(input("Digite o vetor de pontos x0;x1;x1;{...};xn : ")))
x = x.astype(float)
y = np.matrix(eval(input("Digite o vetor de pontos f(x0);f(x1);{...};f(xn) :")))
x = x.astype(float)
n = x.shape[0] # quantidade de linhas de x = quantidade de pontos

v = np.zeros([n,n])

v[:,0] = 1

for i in range(1,n):

    v[:,i] = np.transpose(np.power(np.copy(x),i))


v = np.hstack((np.copy(v),np.copy(y)))

start = timer()

r = resolveTriangular(pivotacaoParcial(v)[0])[1]

end = timer()

st = ""

for j in range(0,r.shape[1]):

    if(j == 0): # se for o termo independente
        if(r[0,j] > 0):
            st += " + "+str(r[0,j])
        elif(r[0,j] < 0):
            st += " "+str(r[0,j])

    elif(j != r.shape[0]-1):

        if(r[0,j] > 0):
            st += " + "+str(r[0,j])+"*x**"+str(j)
        elif(r[0,j] < 0):
            st += " "+str(r[0,j])+"*x**"+str(j)

x = symbols('x')
st = sympify(str(st))

x0 = float(input("Digite um valor de x para ser testado no polinômio da interpolação: "))

print("y(x) = ",str(st))
print("y("+str(x0)+"): ",st.subs(x,x0))
print("Tempo de execucao total: %e segundos" % (end - start))
        
    
