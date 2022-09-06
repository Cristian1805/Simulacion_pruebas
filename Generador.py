import numpy as np;


def Generador (a,c,m,xn1):


    Salida = np.array([xn1])

    for i in range(0,2*m):
        Xn = (a*xn1+c) % m
        Salida = np.append(Salida,Xn)
        xn1 = Xn

    return Salida

print (Generador(17,43,100,27)) 
print (Generador(5,6,8,4))