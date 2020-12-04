print ("Ejercicio12")
print ("José Adrián Criollo Jiménez")
print("Programa para calcular el valor total de una factura con descuentos")

#Inicializacion de variables

subtotal = float (0)
total = float (0)
descuentos = float (0)
limite1 = 200
limite2 = 500

#Ingresar datos de entrada

subtotal = float (input ("Ingrese el subtotal de la compra: "))
subtotal = float(subtotal)

#Proceso

if subtotal >= limite1 and 100 >= limite2:
	descuentos = 0.10

else:
	if subtotal >= limite2:
		descuentos = 0.15

if subtotal < limite1:
	print ('No hay un descuento por su compra por que el valor es menor a 200 dolares')

total= subtotal - (subtotal * descuentos)

#Presenta la salida de resultados
print ("El tota de la factura es: " ,total,  " con un descuento de " ,descuentos)
