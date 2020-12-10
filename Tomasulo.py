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
	for estRes in listaEr:
		#Seleciona somente as ER que possuem a OP(por exemplo, as ER relacionadas a Mult ou add)
		#POR ENQUANTO RETORNA UM NONE TYPE PARA O CALLER, TEM Q ARRUMAR.(POR ISSO A CHECAGEM NO DESPACHO)
		if estRes.tipo[:-1] == op:
			if estRes.busy == False:
				return estRes 

def Despacho(listaInstr,eR):
	for instrucao in listaInstr:
 		##UPF
		if instrucao.tipo == 'Ari':
			ErRelacionada = CheckBusy(eR,instrucao.op)
			##CHECAGEM DESNECESSARIA, PRECISA DE FIX.
			if isinstance(ErRelacionada,EstRes):
				a = ErRelacionada 
			if instrucao.rs.qi != 0:
				a.qj = instrucao.rs.qi
			else:
 				#print(ErRelacionada)
				a.vj = instrucao.rs.valor
				a.qj = 0
			if instrucao.rt.qi != 0:
				a.qk = instrucao.rs.qi
			else:
				a.vk = instrucao.rs.valor
				a.qk = 0
			a.busy = True
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
