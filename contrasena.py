#coding=utf-8
# Programa que pida una contraseña y rechace al usuario
#despues de 5 intentos

import time 

password="guajolotitos"
correcto=0
intentos=1

print("Bienvenido al Centro Educativo Patria")

while(correcto==0) & (intentos<=4):
	intento=input("Intoduce tu contraseña:")
	if intento==password:
		correcto=1
		print("Tu contaseña es correcta!")
	else:
		time.sleep(5)
		print("La contraseña que has introducido es incorrecta")
		intentos=intentos +1 
		if intentos>4:
print("Has introducido demasiadas contraseñas incorrectas")




 	
