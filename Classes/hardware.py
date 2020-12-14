from .registradores import Registradores


class EstRes():
	def __init__(self,tipo):
		self.tipo = tipo
		self.op = None
		self.qj = 0
		self.qk = 0
		self.vj = 0
		self.vk = 0
		self.a = 0
		self.busy = False

	def reset(self):
		self.op = None
		self.qj = 0
		self.qk = 0
		self.vj = 0
		self.vk = 0
		self.a = 0
		self.busy = False

	def __str__(self):
		return '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t'.format(self.tipo, self.busy, self.op,self. vj,self.vk, self.qj, self.qk, self.a)
 

class Memoria():
	def __init__(self,size = 1024):
 		self.data = [0 for i in range(size)]

	def get(self,idx):
 		return self.data[idx]

	def set(self,idx,inpt):
 		self.data[idx] = inpt

	def reset(self):
 		self.data = [0 for i in range(len(self.data))]


class _UF:
	def __init__(self,rd = None,rs = None,rt = None, imm = None ):
		self.resultado = 0
		self.busy = False
		self.cicloInicial = 0
		self.cicloFinal = 0
		self.rs = rs
		self.rt = rt
		self.imm = imm
		self.rd = rd

	def reset(self):
		self.resultado = 0
		self.busy = False
		self.cicloInicial = 0
		self.cicloFinal = 0
		self.rs = None
		self.rt = None
		self.imm = None
		self.rd = None
	
	def __repr__(self):
		return '{}\t{}\t{}\t'.format(self.cicloInicial,self.cicloFinal,self.busy)

class Adder(_UF):
	def __init__(self):
		super().__init__()
		 

class Multiplier(_UF):
	def __init__(self):
		super().__init__()

class MemoUnit(_UF):
	def __init__(self):
		super().__init__()