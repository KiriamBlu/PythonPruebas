
languajes = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf'
}

if (isinstance(languajes, tuple) and len(languajes) == 0):
	print("No history here")

def historycreator(languajes):
	for fill in languajes.items():
		print("%s was created by %s" % fill)

historycreator(languajes)