#coding=utf-8
print("Hola  mundo")
nombre1 = input("Dame el nombre de la primera persona:")
nombre2 = input("Dame el nombre de la segunda persona:")
edad1 = int(input("Dame tu edad %s:" % nombre1))
edad2 = int(input("Dame tu edad %s:" % nombre2))
if(edad1<edad2):
	print("%s es mayor que" % nombre2)
elif(edad2>edad1):
	print("%s es menor que" % nombre1)
else:
	print("%s y %s tienen la misma edad." % (nombre1, nombre2))



         














