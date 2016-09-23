#coding=utf-8
#Programa que pida una contrasena y rechace al usuario
#despues de cinco intentos

import time

password = "Miranda es gay"
correcto = 0
intentos = 1

print("Bienvenido al Centro Educativo Patria.")


while (correcto == 0) & (intentos <=4):
	intento = input ("Introduce tu contrasena:")
	if intento == password:
		correcto = 1
		print("Tu contrasena es correcta!")
	else:
		time.sleep(5)
		print("La contrasena que has introducido es incorrecta.")
		intentos = intentos + 1
		if intentos > 4:
			print("Has introducido demasiadas contrasenas incorrectas.")
