print ("Ejercicio8")
print ("José Adrián Criollo Jiménez")

print ("Programa para saber cual es el mayor de tres numeros ")
print ("Estructura en condiciones simples")

#Declaracion de variables

Num1 = 0
Num2 = 0
Num3 = 0
Mayor = 0
Menor = 0
R = 0
String = "" 

#Datos de entrada

Num1 = int(input("Ingrese el primer número "))
Num1 = int(Num1)
Num2 = int(input("Ingrese el segundo número "))
Num2 = int(Num2)
Num3 = int(input("Ingrese el tercer número "))
Num3 = int(Num3)

#Proceso

if Num1 > Num2 and Num1 > Num3:
       R = println('El numero mayor que has ingresado es: ' ,Num1)
if Num2 > Num1 and Num2 > Num3:
       R = print('El numero mayor que shas ingresado es: ' ,Num2)
if Num3 > Num1 and Num3 > Num2:
       R = print('El numero mayor que has ingresado es: ' ,Num3)
print ("El numero mayor es: ")

print ("Programa para saber cual es el mayor de tres numeros ")
print ("Estructura en condiciones compuestas")


#Datos de entrada

Num1 = int(input("Ingrese el primer número "))
Num1 = int(Num1)
Num2 = int(input("Ingrese el segundo número "))
Num2 = int(Num2)
Num3 = int(input("Ingrese el tercer número "))
Num3 = int(Num3)

#Proceso

if Num1 > Num2 and Num1 > Num3:
       R = print('El numero mayor que has ingresado es: ' ,Num1)
else:
	print ()

if Num2 > Num1 and Num2 > Num3:
       R = print('El numero mayor que has ingresado es: ' ,Num2)
else:
	print ()

if Num3 > Num1 and Num3 > Num2:
       R = print('El numero mayor que has ingresado es: ' ,Num3)
else:
	print ()

print ("El numero mayor es: ")

print ("Programa para saber cual es el mayor de tres numeros ")
print ("Estructura en condiciones anidadas")

#Datos de entrada

Num1 = int(input("Ingrese el primer número "))
Num1 = int(Num1)
Num2 = int(input("Ingrese el segundo número "))
Num2 = int(Num2)
Num3 = int(input("Ingrese el tercer número "))
Num3 = int(Num3)

#Proceso
if Num1 > Num2 and Num1 > Num3:
       	R = print('El numero mayor que has ingresado es ' ,Num1)
else:
	print() 
	if Num2 > Num1 and Num2 > Num3:
       		R = print('El numero mayor que has ingresado es ' ,Num2)
	else:
		print()

		if Num3 > Num1 and Num3 > Num2:
       			R = print('El numero mayor que has ingresado es ' ,Num3)
		else:
			print ()
