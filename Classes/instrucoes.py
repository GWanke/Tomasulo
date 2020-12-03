from .config import Config

class Instrucoes():

	def __init__(self,linha):
		linha = linha.split()
		##pega o operator
		self.op = linha[0]
		##pega os registradores
		self.registradores = linha[1]
		# if registradores[0] not in Config.Desvios and registradores[0] != 'sw':
		# 	self.rd = registradores[0]
		# 	if registradores[1] != ''
		# 	self.rs = registradores[1]
	def __repr__(self):
		return 'Operacao {}\tRegistradores{}'.format(self.op,self.registradores)




