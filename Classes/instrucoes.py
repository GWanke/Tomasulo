from .config import Config
from .registradores import Registradores

class Instrucoes():

	def __init__(self,linha):
		linha = linha.split()
		self.op = linha[0]
		self.ciclos = Config.Tempo.get(self.op.lower())
		self.despacho = None
		self.execCompleta = None
		self.escrita = None
		self.rd = None
		self.rs = None
		self.rt = None
		self.imm = None
		self.Tipo(linha[1].split(',')) 

	def Tipo(self,string):
		if self.op.lower() in Config.Aritmeticas:
			self.tipo = 'Ari'	
			for idx,substring in enumerate(string):
				if idx == 0:
					self.rd = Registradores(substring[1:])
				elif idx == 1:
					self.rs = Registradores(substring[1:])
				else:
					if substring.startswith('F'):
						self.rt = Registradores(substring[1:])
					else:
						self.imm = substring
		elif self.op.lower() in Config.Logicas:
			self.tipo = 'Log'
			for idx,substring in enumerate(string):
				if idx == 0:
					self.rd = Registradores(substring[1:])
				elif idx == 1:
					self.rs = Registradores(substring[1:])
				else:
					self.rt = Registradores(substring[1:])
		elif self.op.lower() in Config.Desvios:
			self.tipo = 'Dvo'
			for idx,substring in enumerate(string):
				if idx == 0 and self.op.lower() != 'j':
					self.rs = Registradores(substring[1:])
				elif idx == 0 and self.op.lower() =='j':
					self.imm = substring
				elif idx == 1:
					self.rt = Registradores(substring[1:])
				else:
					self.imm = substring
		elif self.op.lower() in Config.Memoria:
			self.tipo = 'Mem'
			for idx,substring in enumerate(string):
				if idx == 0 and self.op.lower() == 'lw':
					self.rd = Registradores(substring[1:])
				elif idx == 0 and self.op.lower() == 'sw':
					self.rt = Registradores(substring[1:])
				elif idx == 1:
					#print(substring[3:5])
					self.rs = Registradores(substring[4:5])
					self.imm = substring[0:2]+'+'+substring[3:5]

	def __repr__(self):
		return '{}\n---RD {}\tRS {}\tRT {}\tIMM {}'.format(self.op,self.rd,self.rs,self.rt,self.imm)


