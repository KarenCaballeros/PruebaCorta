from collections import deque

def es_palindromo(palabra):
	cola= deque([])
	pila = []
	prueba= []
	prueba2= []
	for letra in palabra:
		pila.append(letra)
	for letra in palabra:
		prueba.append(pila.pop())
		cola.append(letra)
		prueba2.append(cola.popleft())
	if prueba == prueba2:
		return True
	return False		