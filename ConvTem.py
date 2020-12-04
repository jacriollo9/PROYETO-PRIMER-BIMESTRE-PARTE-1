print ("Ejercicio9")
print ("José Adrián Criollo Jiménez")
print ("Programa para convertir de grados Centigrados a grados Farenhey y a grados Kelvin")

#Inicializar y declarar las variables
gC = float (0)
gF = float (0)
gK = float (0)

gC = float (input ("Ingrese los grados centigrados"))
gC = float(gC)

#Condicio para conversion de grados de temperatura

if gC > 0:
	gF = (gC * 9/5) + 32
	gK = (gC + 273.15)

	print ("La equivalencia en grados farenhey es: " ,gC)
	print ("La equivalencia en grados kelvin es: " ,gK)

