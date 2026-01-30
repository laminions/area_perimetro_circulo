# programa para calcular el area y el perimetro de un circulo de radio R

# librerias 
import math 

print("-------------------------------------") 
print("-----Area y perimetro del circulo----")
print("-------------------------------------")

# input 
r = input("ingrese el valor del radio del circulo: ")
r = int(r)

# processing }
a = math.pi*r**2
p = 2*math.pi*r

#output
print("--------------------------------------")
print("--------------resultados--------------")
print("--------------------------------------")
print("El area del circulo es: "+str(a))
print("el perimetro del circulo es: " + str (p))
print("----------------------------------------")
