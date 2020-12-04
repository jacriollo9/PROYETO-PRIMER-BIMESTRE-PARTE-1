print ("Ejercicio3")
print ("Programa para saber el area del poligeno")
print ("José Adrián Criollo Jiménez")

print ("Area del Poligeno")
#	Declaración de variables


# Lectura de datos
lc=float(input("Ingrese el lado de el cuadrado " ))
A=lc**2
print('El área de el cuadrado es',A )

at = float(input("Ingrese la altura de el triángulo " ))
B=(lc+at)//2
print('El área de el triángulo  es', B )


ar=float(input("Ingrese la altura de el rectangulo " ))
D=lc*ar
print ('El área de el rectangulo  es ',D )

ats= at*3
print('EL área de los tres triángulos es ', ats )

area= A+ats+D
print('El area polígono es ' ,area )

# Salida de datos
print('El área del polígono compuesto es: ', area, 
	'compuesto por un cuadrado de lado' , lc,'un rectángulo de altura',
	 ar, 'y una altura de triángulo',at )
