from Classes.config import Config
from Classes.instrucoes import Instrucoes

def readInput():
	with open('Testes/teste.txt') as f:
		for line in f:
			##garante que soh sera passado uma linha/vez. (lazy iterator)
			yield Instrucoes(line)
			

def main():
	i = []
	i = readInput()
	for item in i:
		print (item)
		for registradores in item.vLista:
			print (registradores)
if __name__ == '__main__':
    main()
