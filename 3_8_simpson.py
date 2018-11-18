import numpy as np
from sympy import *
from math import *

def regra_3_8_Simpson(fx,a,h,x):

    return ((3*h)*(fx.subs(x,a) + 3*fx.subs(x,a+h) + 3*fx.subs(x,a+2*h) + fx.subs(x,a+3*h)))/8

x = symbols('x')

fx = sympify(str(input("Digite a função f(x): ")))
a = float(input("Digite o começo do intervalo de integração: "))
b = float(input("Digite o fim do intervalo de integração: "))
t = float(input("Digite o modo de integração: (0 - sem repetição, 1 - com repetição): "))

if(t == 0):

    Ir = integrate(fx,(x,a,b))
    Ia = regra_3_8_Simpson(fx,a,abs(b-a)/4,x)
    print("Integral aproximada: ",Ia)


elif(t == 1):

   m = int(input("Digite a quantidade m de intervalos: "))

   h = float(abs(b-a)/m)

   if(m*h == (b-a) and m%3 == 0):
        Ia = 0
        for i in range(0,m,3):
            Ia += regra_3_8_Simpson(fx,a,h,x)
            a += 3*h

        print("Integral aproximada: ",Ia)
   else:
        print("m é inválido")
       

