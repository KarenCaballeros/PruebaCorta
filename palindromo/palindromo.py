from collections import deque

def es_palindromo(palabra):
	cola= deque([])
	pila = []
	for letra in palabra:
		cola.append(letra)
		pila.append(letra)

	if cola.popleft() == pila.pop():
		es_palindromo(cola)
		return True

	return False		