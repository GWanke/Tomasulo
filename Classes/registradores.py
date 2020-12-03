class Registradores():
	def __init__(self):
		self.status = None
		self.valor = 0
		self.indice = 0

	def __str__(self):
		return 'Indice = {}\tStatus = {}\tValor =  {}'