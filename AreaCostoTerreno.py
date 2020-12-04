print ("Ejercicio 4")
print ("Programa que permita calcular el area del terreno")
print ("José Adrián Criollo Jiménez")

A = 0
B = 0
C = 0
D = 0
at = 0
ar = 0 


A = float (input("Ingrese la altura del paralelogramo ")) 
B = float (input("Ingrese el largo del paralelogramo ")) 
C = float (input("Ingrese la altura del paralelogramo ")) 
D =  A**C
print ('La altura del triangulo es: ', D)
at = (B*A)//2
print('El area del triangulo es: ', at)
ar = B*C
print('El area del rectangulo es: ', ar )
areatotal = at + ar

print ('El area del terreno compuesto es: ', areatotal, 'compuesto por un ractangulo de largo', A, 'un rectangulo de largo' , B,
	'y una altura de rectangulo',C)

Costo_Terreno = float(input("Ingrese el costo de metro cuadrado"))
print (Costo_Terreno)
Area_Total = float (input("Ingresa el area total del paralelogramo"))
Costo_Terreno = print ('El costo total del terreno es: ', Area_Total * Costo_Terreno)
