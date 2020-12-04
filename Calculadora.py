print ("Ejercicio11")
print ("José Adrián Criollo Jiménez")
print ("Programa para hacer operaciones basicas")

#Inicialización de variables

num1=float(0)
num2=float(0)
resp=float(0)
opc=int(0)

#Ingreso de datos
while (True):

	print("Programa de calculadora básica \n ")

	num1=float(input("Ingrese un número : "))
	num2=float(input('Ingrese el otro número: '))

	#Proceso
	print('Selecciona la operación que deseas realizar :')
	print('1. Suma')
	print('2. Resta')
	print('3. Múltiplicación')
	print('4. Dividir')
	opc= int(input('Elija la opción: '))

	if opc==1:
		resp= num1+num2
		print(resp)

	if opc ==2:
		resp= num1-num2
		print(resp)

	if opc == 3:
		resp = num1* num2
		print(resp)

	if opc== 4 :
		resp= num1//num2
		print (resp)
