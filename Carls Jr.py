#coding=utf-8
#Programa que tome la orden en el Carls Junior
#Con 5 opciones en el menu
costo = 0 
pedido = 1
print("Bienvenido a Carls Jr, te atiende Andres.")

print ('''1. Famouse Star ($90)
2. Papas Grandes ($40)
3. Santa Fe ($100)
4. Soda Grande ($30)
5. Salida ''')
while(pedido <5):
	orden = int(input("Elige tu orden: "))

	if orden == 1:
		costo = costo + 90
	elif orden == 2:
		costo = costo + 40
	elif orden == 3:
		costo = costo + 100	
	elif orden == 4:
		costo = costo + 30
   
	print  ("El total de su orden es: %s" % costo)




 	
