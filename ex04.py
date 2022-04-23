
import sys

class calculator:
	def __init__(self):
		self._sum = 0
		self._substra = 0
		self._product = 0
		self._div = 0
		self._modul = 0
	def sum(self, n1 = 0, n2 = 0):
		self._sum = int(n1) + int(n2)
	def substra(self, n1 = 0, n2 = 0):
		self._substra = int(n1) - int(n2)
	def product(self, n1 = 0, n2 = 0):
		self._product = int(n1) * int(n2)
	def div(self, n1 = 0, n2 = 0):
		self._div = int(n1) / int(n2)
	def modul(self, n1 = 0, n2 = 0):
		self._modul = int(n1) % int(n2)

if len(sys.argv) != 3:
	print("ERROR")
	exit(0)
inputs = calculator()

inputs.sum(sys.argv[1], sys.argv[2])
inputs.substra(sys.argv[1], sys.argv[2])
inputs.product(sys.argv[1], sys.argv[2])
inputs.div(sys.argv[1], sys.argv[2])
inputs.modul(sys.argv[1], sys.argv[2])

print("Sum: ", inputs._sum)
print("Differece: ", inputs._substra)
print("Product: ", inputs._product)
if int(sys.argv[1]) != 0 and int(sys.argv[2]) != 0:
	print("Quotient: ", inputs._div)
else:
	print("Being divided by 0")
if int(sys.argv[1]) != 0 and int(sys.argv[2]) != 0:
	print("Remainder: ", inputs._modul)
else:
	print("Being moduled by 0")