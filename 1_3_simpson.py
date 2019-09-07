# -*- coding: utf-8 -*-

import numpy as np
from sympy import *
from math import *

def regra_1_3_Simpson(fx,a,h,x):

    return ((h)*(fx.subs(x,a) + 4*fx.subs(x,a+h) + fx.subs(x,a+2*h)))/3


x = symbols('x')

fx = sympify(str(input("\n\n   Digite a função f(x): ")))
a = float(input("   Digite o começo do intervalo de integração: "))
b = float(input("   Digite o fim do intervalo de integração: "))
t = float(input("   Digite o modo de integração: (0 - sem repetição, 1 - com repetição): "))

if(t == 0):

    Ir = integrate(fx,(x,a,b))
    Ia = regra_1_3_Simpson(fx,a,abs(b-a)/2,x)
    print("   Integral aproximada: "+str(Ia)+"\n\n")

elif(t == 1):

   m = int(input("   Digite a quantidade m de intervalos: "))

   h = float(abs(b-a)/m)

   Et = -(h**5/90)*diff(diff(diff(diff(fx,x),x),x),x)

   Es = Et.subs(x,a)

   if(m%2 == 0 and m*h == (b-a)):
        Ia = 0
        for i in range(0,m-1,2):
            Es += Et.subs(x,a+h)
            Ia += regra_1_3_Simpson(fx,a,h,x)
            a += 2*h

        print("   Integral aproximada: "+str(Ia)+"\n\n")
   else:
        print("   Erro: m não é múltiplo de 2\n\n")
       

