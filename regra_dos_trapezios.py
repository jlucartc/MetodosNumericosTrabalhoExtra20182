# -*- coding: utf-8 -*-


import numpy as np
from sympy import *
from math import *

def regraDosTrapezios(fx,a,b,x):

    return ((b-a)*(fx.subs(x,a) + fx.subs(x,b)))/2


x = symbols('x')

fx = sympify(str(input("\n\n   Digite a função f(x): ")))
a = float(input("   Digite o começo do intervalo de integração: "))
b = float(input("   Digite o fim do intervalo de integração: "))
t = float(input("   Digite o modo de integração: (0 - sem repetição, 1 - com repetição): "))

if(t == 0):

    Ia = regraDosTrapezios(fx,a,b,x)
    print("   Integral aproximada: "+str(Ia)+"\n\n")

elif(t == 1):

   m = int(input("   Digite a quantidade m de divisões: "))

   h = abs(b-a)/m

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
        print("   Integral aproximada: "+str(Ia)+"\n\n")
   else:
        Ia = 0
        xk = a
        for i in range(0,m):
            Et += -(h**3/12)*(diff(diff(fx,x),x).subs(x,a+h))
            Ia += regraDosTrapezios(fx,a,(a+h),x)
            a += h

        print("   Integral aproximada: "+str(Ia)+"\n\n")

