from Classes.config import Config
from Classes.instrucoes import Instrucoes
from Classes.registradores import Registradores
from Classes.hardware import *

class Tomasulo():
	def __init__(self,instrucL):
		#Program counter
		self.pc = 0
		self.clock = 0
		self.registradores = [Registradores(i) for i in range(Config.registradores)]
		self.memoria = Memoria()
		self.adderL = [Adder() for _ in range(Config.SS)]
		self.mulL = [Multiplier() for _ in range(Config.MD)]
		self.memL = [MemoUnit() for _ in range(Config.LS)]
		self.instrucL = instrucL
		self.ersL = estacoesR()

	def printER(self):
		for er in self.ersL:
			print(er)

	def printReg(self):
		print('REGISTRADORES\n')
		for registradorIdx in range(len(self.registradores)):
			print("F[{0}] {1}".format(registradorIdx,self.registradores[registradorIdx]),end = '\t')

	def pronto(self):
		#retorna True se o algoritmo finalizar(Todos as instrucoes possuem algum ciclo relativos ao write.)
		if all([x.escrita for x in self.instrucL]):
			return True
		else:
			return False
	def passo(self):
		while not self.pronto():
			if self.pc in range(len(self.instrucL)):
				instrAtual = self.instrucL[self.pc]
				estR = self.preDespacho(instrAtual)
				if estR != -1:
					#Despacha a instrucao e incrementa o PC.
					ErUtilizada = self.Despacho(estR,instrAtual)
					self.pc +=1
				self.preExecute(instrAtual)
			else:
				break
			#self.printER()
			#self.printReg()
			self.clock += 1
			print()
			a = input('Pressione enter para o proximo clock!')
	

	def preDespacho(self,instrAtual):
	#RETORNA -1 CASO TODAS ESTIVEREM OCUPADAS.
		listaADD = self.ersL[0:8]
		listaMUL = self.ersL[8:16]
		buffersLW = self.ersL[16:24]
	##UPF
		if instrAtual.op == 'ADD' or instrAtual.op == 'SUB':
			if all([x.busy for x in listaADD]):
				return -1
			else:
				for estacao in listaADD:
					if estacao.busy is False:
						estacao.op = instrAtual.op
						return estacao
		elif instrAtual.op =='MUL' or instrAtual.op == 'DIV':
			if all([x.busy for x in listaMUL]):
				return -1
			else:
				for estacao in listaMUL:
					if estacao.busy is False:
						estacao.op = instrAtual.op
						return estacao
		##LOAD/STORE
		elif instrAtual.op =='LW' or instrAtual.op == 'SW':
			if all([x.busy for x in buffersLW]):
				return -1
			else:
				for bufferR in buffersLW:
					if bufferR.busy is False:
						bufferR.op = instrAtual.op
						return bufferR

	def Despacho(self,ErRelacionada,instrucao):
		if instrucao.rd is not None:
		 	rdIDX = instrucao.rd.indice
		if instrucao.rt is not None:
		 	rtIDX = instrucao.rd.indice
		if instrucao.rs is not None:
		 	rsIDX = instrucao.rd.indice
		instrucao.despacho = self.clock
		##UPF
		if instrucao.tipo == 'Ari': 
			if instrucao.rs.qi != 0:
				ErRelacionada.qj = self.registradores[rsIDX].qi
			else:
				ErRelacionada.vj = self.registradores[rsIDX].valor
				ErRelacionada.qj = 0
			if instrucao.rt.qi != 0:
				ErRelacionada.qk = self.registradores[rtIDX].qi
			else:
				ErRelacionada.vk = self.registradores[rtIDX].valor
				ErRelacionada.qk = 0
			ErRelacionada.busy = True
			self.registradores[rdIDX].qi = ErRelacionada.tipo
		elif instrucao.tipo == 'Mem':
			#LOAD
			if instrucao.op == 'LW':
				if instrucao.rs.qi != 0:
					ErRelacionada.qj = self.registradores[rsIDX].qi
				else:
					ErRelacionada.vj = self.registradores[rsIDX].valor
					ErRelacionada.qj = 0
				ErRelacionada.a = instrucao.imm
				ErRelacionada.busy = True
				self.registradores[rdIDX].qi = ErRelacionada.tipo
				#print(instrucao.rd.qi)
			#STORE
			if instrucao.op == 'SW':
				if instrucao.rs.qi != 0:
					ErRelacionada.qj = self.registradores[rsIDX].qi
				else:
					ErRelacionada.vj = self.registradores[rsIDX].valor
					ErRelacionada.qj = 0
				if instrucao.rt.qi != 0:
					ErRelacionada.qk = self.registradores[rsIDX].qi
				else:
					ErRelacionada.vk = self.registradores[rsIDX].valor
					ErRelacionada.qk = 0
				ErRelacionada.a = instrucao.imm
				ErRelacionada.busy = True
		return ErRelacionada

	def preExecute(self,instruc):
		#UFP
		if instruc.op == 'ADD' or instruc.op == 'SUB':
			if all([x.busy for x in self.adderL]):
				adderE = -1
			else:
				for adder in self.adderL:
					if adder.busy is False:
						adderE = adder
						adderE.cicloInicial = self.clock
						adderE.cicloFinal = adderE.cicloInicial + instruc.ciclos
						adderE.rd = instruc.rd.valor
						adderE.rs = instruc.rs.valor
						adderE.rt = instruc.rt.valor
		elif instruc.op == 'DIV' or instruc.op =='MUL':
			if all([x.busy for x in self.mulL]):
				mulE = -1
			else:
				for mul in self.adderL:
					if mul.busy is False:
						mulE = mul
						mulE.cicloInicial = self.clock
						mulE.cicloFinal = mulE.cicloInicial + instruc.ciclos
						mulE.rd = instruc.rd.valor
						mulE.rs = instruc.rs.valor
						mulE.rt = instruc.rt.valor
		#LOAD
		###CONTINUAR DAQUI

	def Execute(self):
		pass
print("Nome\tBusy\tOp\tVj\tVk\tQj\tQk\tA")


def readInput():
	with open('Testes/teste2.txt') as f:
		for line in f:
			yield Instrucoes(line)

def estacoesR():
	#CRIACAO DAS ESTACOES RESERVA.
	mat = []
	for num in range(1,25):
		if num <= 8:
			mat.append(EstRes('ADD{}'.format(num)))
		elif num > 8 and num <= 16:
			mat.append(EstRes('MUL{}'.format(num - 8)))
		else:
			mat.append(EstRes('LOAD{}'.format(num - 16)))
	return mat

	


def main():
	entrada = readInput()
	listaEntrada = list(entrada)
	tomasulo = Tomasulo(listaEntrada)
	tomasulo.passo()
if __name__ == '__main__':
    main()
