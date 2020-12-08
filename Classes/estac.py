from .registradores import Registradores


class ER():
	def __init__(self,tipo):
		self.tipo = tipo
		self.op = None
		self.qj = 0
		self.qk = 0
		self.vj = 0
		self.vk = 0
		self.a = 0
		self.busy = False

	def __str__(self):
		return '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t'.format(self.tipo, self.busy, self.op,self. vj,self.vk, self.qj, self.qk, self.a)