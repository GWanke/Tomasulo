class Registradores():
	def __init__(self,idx):
		self.indice = int(idx)
		self.valor = 0
		self.qi = 0
		self.EndMem = hex(self.indice)

	def reset(self):
		self.valor = 0
		self.qi = 0		

	def __str__(self):
		return 'Indice = F{}\tValor = {}\tQi = {}\t,Mem = {}\n'.format(self.indice,self.valor,self.qi,self.EndMem)