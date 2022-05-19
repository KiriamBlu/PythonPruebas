

import sys


class sentence:
	def __init__(self, string = ""):
		self._string = string
		self._upper = 0
		self._lower = 0
		self._spaces = 0
		self._puntuation = 0

mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'
puntuacion = '.,;!?¿¡'

if len(sys.argv) != 2:
	print("ERROR")
	exit(0)
inputs = sentence(sys.argv[1])
y = len(inputs._string)
x = 0

for x in range(1, y):
	if inputs._string[x] == ' ':
		inputs._spaces += 1;
	elif inputs._string[x] in minusculas:
		inputs._lower += 1;
	elif inputs._string[x] in mayusculas:
		inputs._upper += 1;
	elif inputs._string[x] in puntuacion:
		inputs._puntuation += 1;

print("Upper letters: ",inputs._upper)
print("Lower letters: ",inputs._lower)
print("Space letters: ",inputs._spaces)
print("Puntuation letters", inputs._puntuation)