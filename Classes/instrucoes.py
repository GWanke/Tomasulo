from .config import Config
from .registradores import Registradores

class Instrucoes():

	def __init__(self,linha):
		linha = linha.split()
		##pega o operator
		self.op = linha[0]
		##pega os registradores
		self.valores = linha[1].split(',')
		##lista de valores
		self.vLista = []
		for valor in self.valores:
			##Identifica um registrador,caso o valor comece com 0.
			if valor.startswith('F'):
				aux = Registradores()
				aux.indice = int(valor[1:])
				self.vLista.append(aux)
			# else if valor.endswith(')'):
			# 	valor.split('')
			# else:
			# 	hexadecimal = int(valor,16)
			# 	self.vLista.append(hexadecimal)
		# if registradores[0] not in Config.Desvios and registradores[0] != 'sw':
		# 	self.rd = registradores[0]
		# 	if registradores[1] != ''
		# 	self.rs = registradores[1]
	def __repr__(self):
		return 'Operacao {}\tRegistradores{}'.format(self.op,self.valores)




