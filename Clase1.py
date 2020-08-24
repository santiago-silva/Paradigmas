def ejercicio1():
	oracion = "Hello World"
	print(oracion)

# Imprimir los numeros de 0 a 100 que sean divisibles por 3
def ejercicio3():
	
	for number in range (0, 101):
		if number % 3 == 0:
			print(number)

def ejercicio5():
	
	userValueList = []
	for number in range(10):
		
		userValue = int(input("Ingrese un numero: "))
		userValueList.append(userValue)
	
	userValueList.sort()
	print(userValueList)


def ejercicio6(number1, number2):
	if number1 > number2:
		return 1
	elif number1 == number2:
		return 0
	else:
		return -1
	
def main():
	#ejercicio1()
	#ejercicio3()
	#ejercicio5()
	
	userInput1 = int(input("ingrese el numero 1: "))
	userInput2 = int(input("ingrese el numero 2: "))
	
	print(ejercicio6(number1, number2))
	
main()