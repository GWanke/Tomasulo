from Classes.config import Config
from Classes.instrucoes import Instrucoes
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

def Despacho(listaInstr):
	##UPF
	for instrucao in listaInstr:
		print(instrucao)
		#input()




def main():
	i = []
	i = readInput()
	tabela = estacoesR()
	#for item in tabela:
		#print(item)
	Despacho(i)
if __name__ == '__main__':
    main()
