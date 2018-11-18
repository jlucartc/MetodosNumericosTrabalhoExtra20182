import numpy as np
from sympy import *
from math import *

def regraDosTrapezios(fx,a,b,x):

    return ((b-a)*(fx.subs(x,a) + fx.subs(x,b)))/2


x = symbols('x')

fx = sympify(str(input("Digite a função f(x): ")))
a = float(input("Digite o começo do intervalo de integração: "))
b = float(input("Digite o fim do intervalo de integração: "))
t = float(input("Digite o modo de integração: (0 - sem repetição, 1 - com repetição): "))

if(t == 0):

    Ir = integrate(fx,(x,a,b))
    Ia = regraDosTrapezios(fx,a,b,x)
    print("Integral aproximada: ",Ia)
    print("Integral real: ",Ir)
    
    print("Erro: "+str((abs(Ir-Ia)/abs(Ir))*100)+"%")


elif(t == 1):

   h = float(input("Digite o tamanho h dos intervalos das repetições: "))

   m = floor(abs(b-a)/h)

   Et = (-h**3/12)*diff(diff(fx,x),x).subs(x,a)

   if(m*h < (b-a)):
        hEx = (b-a) - h*m
        Ia = 0
        xk = a
        for i in range(0,m+1):
            if(i == m):
                Et += -(h**3/12)*diff(diff(fx,x),x).subs(x,a+hEx)
                Ia += regraDosTrapezios(fx,a,(a+hEx),x)
                a += hEx
            else:
                Et += -(h**3/12)*diff(diff(fx,x),x).subs(x,a+h)
                Ia += regraDosTrapezios(fx,a,(a+h),x)
                a += h
        print("Integral aproximada: ",Ia)
        print("Somatório do erro: "+str(Et))
   else:
        Ia = 0
        xk = a
        for i in range(0,m):
            Et += -(h**3/12)*(diff(diff(fx,x),x).subs(x,a+h))
            Ia += regraDosTrapezios(fx,a,(a+h),x)
            a += h

        print("Integral aproximada: ",Ia)
        print("Somatório do erro: "+str(abs(Et)))

