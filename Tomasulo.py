from Classes.config import Config
from Classes.instrucoes import Instrucoes
from Classes.registradores import Registradores
from Classes.hardware import *

def readInput():
	with open('Testes/teste2.txt') as f:
		for line in f:
			##garante que soh sera passado uma linha/vez. (lazy iterator)
			yield Instrucoes(line)
			
def estacoesR():
	mat = []
	print("Nome\tBusy\tOp\tVj\tVk\tQj\tQk\tA")
	for num in range(1,25):
		if num <= 8:
			mat.append(EstRes('ADD{}'.format(num)))
		elif num >8 and num <=16:
			mat.append(EstRes('MUL{}'.format(num-8)))
		else:
			mat.append(EstRes('LOAD{}'.format(num-16)))
	return mat

def CheckBusy(listaEr,op):
	if op == 'MUL' or op == 'DIV':
		for estRes in listaEr[8:16]:
			if estRes.busy is False:
				return estRes
	elif op == 'ADD' or 'SUB':
		for estRes in listaEr[0:8]:
			if estRes.busy is False:
				return estRes
	else:
		for estRes in listaEr[16:24]:
			if estRes.busy is False:
				return estRes

def Despacho(listaInstr,eR):
	for instrucao in listaInstr:
 		##UPF
		if instrucao.tipo == 'Ari':
			ErRelacionada = CheckBusy(eR,instrucao.op) 
			if instrucao.rs.qi != 0:
				ErRelacionada.qj = instrucao.rs.qi
			else:
				ErRelacionada.vj = instrucao.rs.valor
				ErRelacionada.qj = 0
			if instrucao.rt.qi != 0:
				ErRelacionada.qk = instrucao.rs.qi
			else:
				ErRelacionada.vk = instrucao.rs.valor
				ErRelacionada.qk = 0
			ErRelacionada.busy = True
			instrucao.rd = ErRelacionada
	for item in eR:
		print (item)




def main():
	i = []
	i = readInput()
	tabela = estacoesR()
	#for item in tabela:
		#print(item)
	Despacho(i,tabela)
if __name__ == '__main__':
    main()
