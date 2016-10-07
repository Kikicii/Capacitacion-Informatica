#coding=utf-8
#Programa para tomar orden 

import time


password="hola"
correcto=0
intentos=1

print("Bienvenido a Carl's Jr., intoduzca la contraseña") 

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
costo=0
pedido=1
print("Hola cliente, qué  llevará hoy?")
print("""1. Famous star $90 
2.Papas grandes $40
3. Santa fe $100
4. Soda grande $30 """)

while (pedido<5): 
	pedido = int(input("Dame tu pedido:"))


	if(pedido==1):
		costo=costo+ 90 
	elif(pedido==2):
		costo=costo+40
	elif(pedido==3):
		costo=costo+100
	elif(pedido==4):
		costo=costo+30

	print("Su orden es de un total de $%s," %(costo)) 
	
else: 
print("Gracias por su visita, buen día.")
