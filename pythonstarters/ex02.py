import sys

n = len(sys.argv)

if n > 2:
	print("TOO MUCH FUCKING ARGUMENTS DUDE")
	exit()
else:
	if sys.argv[1].isdigit():
		if int(sys.argv[1]) == 0:
			print("Este es zero")
		elif int(sys.argv[1]) % 2 == 0:
			print("Este es par")
		else:
			print("Este es impar")
	else:
		print("Esto no ES UN PUTO INT BROTHER")