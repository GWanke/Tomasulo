from Classes.config import Config
from Classes.instrucoes import Instrucoes

def readInput():
	with open('Testes/teste.txt') as f:
		for line in f:
			print(line)

def main():
	readInput()
if __name__ == '__main__':
    main()
