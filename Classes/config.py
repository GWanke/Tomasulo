class Config():
	##unidades de memoria
	#load e store
	LS = 2
	#soma e sub e desvios
	SS = 2
	#mult e div
	MD = 2
	##Quantidade de estacoes de reserva
	SomaeSub = 8
	MulteDiv = 8
	LoadeStore = 8

	##Quantidade de registradores
	registradores = 16

	Aritmeticas = {
		'add' : 5,
		'addi' :  5,
		'sub' : 5,
		'subi' : 5,
		'mul' : 10,
		'div' : 20,
	}

	Logicas = {
		'and' : 5,
		'or' : 5,
		'not' : 5,
	}

	Desvios = {
		'blt' : 5,
		'bgt' : 5,
		'beq' : 5,
		'bne' : 5,
		'j' : 5,
	}

	Memoria = {
		'lw' : 5,
		'sw' : 5,
	}

	##ciclos de clock
	Tempo = {**Aritmeticas, **Logicas, **Desvios, **Memoria}