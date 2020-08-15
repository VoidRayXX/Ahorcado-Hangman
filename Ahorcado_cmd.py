from random import choice
import os
import time
class Juego():
	
	def __init__(self):
		self.palabras = ["MATEMATICAS","FISICA","PROGRAMACION","ETICA","INSTITUTO","PYTHON","PRUEBA","ESPAÑA","UNIVERSIDAD","ESPERANZA","LIBRO","HELICOPTERO",
		"SANGRE","SUERTE","FANTASMA","ESTRATEGIA","AUTOMOVIL","VELERO","INGLATERRA","INFIERNO","INVIERNO","ETERNO","MALVADO","DICCIONARIO","COMPUTADOR","DIARIO",
		"AMENAZA","EXTRATERRESTE","VIAJERO","TRIVIAL","EFIMERO","HIELO","AMOR","PAREJA","OTOÑO","VERANO","FINLANDIA","PRIMAVERA","VACACIONES","LANZAMIENTO",
		"GUERRA","TECNOLOGICO","DEFENSA","ATAQUE","KAISER","PIZZA","INGENIERIA","CALCULO","MAPA","BARCO","PREUNIVERSITARIO","RETORNO","GIGANTE","QUIMERICA","REBELDE",
		"VENERABLE","OLVIDADO","TENEBROSO","ABSOLUTO","IMPLACABLE","CONSIDERABLE","ALEATORIO","TOKIO","SANTIAGO","WASHINGTON","MOSCU","RITMO","JAZZ","ROCK","VIEJO",
		"EFICIENTE","VIENTO","LATIFUNDISTA","TERRORISTA","MONEDA","VALIENTE","INTEGRO","CALIENTE","CALISTENIA","FRIO","VELOCIDAD","ACELERACION","MENSAJE","ITALIA",
		"ROCA","JAZMIN","SECRETO","BONSAI","PEPSI","INFORMATICA","PANDEMIA","VIRUS","MUERTE","VERTICE","CUARENTENA","PROYECTO","MISTERIO","MOLOTOV","ILUSION","MOSCA",
		"PROGRESO","INNOVACION","PALETA","TERMOMETRO","KARATE","FEDERICO","VENGADOR","MERCURIO","OXIGENO","AZUL","HIDROGENO","TRIANGULO","FUTURO","VACIO"]

	def limpiarPantalla(self):
		os.system("CLS")
	
	def displayAhorcado(self,fase,start,victorias,derrotas):
		if not start:
			print("\n\n Ahorcado                        " +  "Victorias: "  + str(victorias) + "    Derrotas: "  +  str(derrotas) + "\n")
		#Nota: los espacios de los dibujos se hicieron con la tecla espacio, no con tabs
		figuras = [
		"  ________\n"+
		" |      |  \n"+
		" |        \n"
		" |     	 \n"+
		" |        \n"+
		" |       \n"+
		" |       \n"+
		" ---------\n\n"
		,
		"  ________\n"+
		" |      |  \n"+
		" |      O  \n"
		" |     	 \n"+
		" |        \n"+
		" |       \n"+
		" |       \n"+
		" ---------\n\n"
		,
		"  ________\n"+
		" |      |  \n"+
		" |      O  \n"
		" |      | \n"+
		" |       \n"+
		" |       \n"+
		" |       \n"+
		" ---------\n\n"
		,
		"  ________\n"+
		" |      |  \n"+
		" |      O  \n"
		" |     /| \n"+
		" |        \n"+
		" |       \n"+
		" |       \n"+
		" ---------\n\n"
		,
		"  ________\n"+
		" |      |  \n"+
		" |      O  \n"
		" |     /|\ \n"+
		" |        \n"+
		" |       \n"+
		" |       \n"+
		" ---------\n\n"
		,
		"  ________\n"+
		" |      |  \n"+
		" |      O  \n"
		" |     /|\ \n"+
		" |      |  \n"+
		" |       \n"+
		" |       \n"+
		" ---------\n\n"
		,
		"  ________\n"+
		" |      |  \n"+
		" |      O  \n"
		" |     /|\ \n"+
		" |      |  \n"+
		" |     /  \n"+
		" |       \n"+
		" ---------\n\n"
		,
		"  ________\n"+
		" |      |  \n"+
		" |      O  \n"
		" |     /|\ \n"+
		" |      |  \n"+
		" |     / \ \n"+
		" |       \n"+
		" ---------\n\n"
		]
		
		print(figuras[fase])
	
	def elegirPalabra(self):
		if len(self.palabras) > 0:
			word = choice(self.palabras)
			self.palabras.remove(word)
			return word
		return "Ya no hay más palabras, completaste el juego:("

	def getPalabra(self,jogo):
		palabra = jogo.elegirPalabra()
		lista_palabra = []
		if ' ' not in palabra:
			for i in range(len(palabra)):
				lista_palabra.append('_ ')
		return lista_palabra,palabra
		
	def trabajarPalabra(self,l):
		#l = lista
		msj = ''
		for i in l:
			msj += i
		print(' ' + msj)
		
	def evaluarVictoria(self,lista):
		for x in lista:
			if '_' in x:
				return False
		return True

	def evaluarDerrota(self,fase):
		if fase == 7:
			return True
		return False

	def evaluar(self,letra,palabra_correcta,l,jogo):
		nueva_lista = list(l)
		if letra == palabra_correcta:
			nueva_lista = list()
			for elemento in palabra_correcta:
				aux = elemento + ' '
				nueva_lista.append(aux)
			return 'victoria',nueva_lista
		elif letra in palabra_correcta:
			indices = []
			for i in range(len(palabra_correcta)):
				if palabra_correcta[i] == letra:
					indices.append(i)
			for x in indices:
				nueva_lista[x] = letra + ' '
			if jogo.evaluarVictoria(nueva_lista):
				return 'victoria',nueva_lista
			return '',nueva_lista
		else:
			if len(letra) > 1:
				return "derrota",nueva_lista
			return "incorrecto",nueva_lista

	def inicio(self,start,victorias,derrotas):
		print("\n\n Bienvenido a Ahorcado!\n")
		juego.displayAhorcado(0,start,victorias,derrotas)
		print("Iniciando juego...")
		print("\nNotas:")
		print("\n1.-El fallar al intentar adivinar la palabra entera implica perder inmediatamente")
		print("2.-Por comodidad, las frases no llevan acento")
		print("3.-No es necesario ingresar las letras/palabras con mayúsculas")
		time.sleep(5)

def continuar(opcion):
	while opcion.lower() != 'si' and opcion.lower() != 'sí' and opcion.lower() != 'no':
		print("\nOpción inválida. Intente de nuevo")
		opcion = input("¿Seguir jugando? (si/no): ")
	if opcion.lower() == 'si' or opcion.lower() == 'sí':
		return True
	else:
		return False

def letrasUsadas(lista):
	msj = ''
	for letra in lista:
		msj += letra + ', '
	print("\n\nLetras ya usadas:",msj)

juego = Juego()
nuevo_juego = True
jugando = True
start = True
victorias = 0
derrotas = 0
juego.inicio(start,victorias,derrotas)
start = False
while nuevo_juego:
	estado = 0
	letras_usadas = []
	lista,word = juego.getPalabra(juego)
	if len(lista) == 0:
		print("\n\n")
		for letra in word:
			lista.append(letra + ' ')
		juego.limpiarPantalla()
		juego.displayAhorcado(0,start,victorias,derrotas)
		juego.trabajarPalabra(lista)
		break
	while jugando:
		juego.limpiarPantalla()
		juego.displayAhorcado(estado,start,victorias,derrotas)
		juego.trabajarPalabra(lista)
		letrasUsadas(letras_usadas)
		eleccion = input("\n Ingrese una letra, o bien, la palabra entera: ").upper()
		evaluacion,lista = juego.evaluar(eleccion,word,lista,juego)
		if evaluacion == 'victoria':
			victorias += 1
			juego.limpiarPantalla()
			juego.displayAhorcado(estado,start,victorias,derrotas)
			juego.trabajarPalabra(lista)
			print("\n\n Felicitaciones, has ganado!")
			decision = input("\n ¿Te gustaría seguir jugando? (si/no): ")
			nuevo_juego = continuar(decision)
			break
		elif evaluacion == 'incorrecto':
			letras_usadas.append(eleccion)
			estado += 1
		elif evaluacion == 'derrota':
			estado = 7
		if juego.evaluarDerrota(estado):
			derrotas += 1
			juego.limpiarPantalla()
			juego.displayAhorcado(7,start,victorias,derrotas)
			lista = []
			for letra in word:
				lista.append(letra + ' ')
			juego.trabajarPalabra(lista)
			print("\n\n Lo siento, perdiste")
			decision = input("\n ¿Te gustaría seguir jugando? (si/no): ")
			nuevo_juego = continuar(decision)
			break
input("\nPresione la tecla Enter para cerrar el programa")