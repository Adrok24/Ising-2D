import random
import cmath


class Particula:
		#Consideramos un casillero como una 4-upla (Letra,fila,columna,validez) de esta forma guarda mas informacion
		
		def __init__(self,f=0,c=0):
			self.magnetizacion= 2*(random.randint(0,1)-1)+1
			self.fil=f
			self.col=c
			self.energia = 0
			
	#Nos da las cordenadas de los casilleros que rodean a un casillero dado 
		def coordEntorno(self,n):
			
			i=self.fil
			j=self.col
			RV=[]
			
			if i == n-1:
				if j == n-1:
					RV.append((n-2,n-1))
					RV.append((n-1,n-2))
					RV.append((n-1,0))
					RV.append((0,n-1))
				elif j == 0:
					RV.append((n-2,0))
					RV.append((n-1,1))
					RV.append((0,0))
					RV.append((n-1,n-1))
				else :
					RV.append((n-2,j))
					RV.append((n-1,j-1))
					RV.append((n-1,j+1))
					RV.append((0,j))
			elif i == 0:
				if j == n-1:
					RV.append((n-1,n-1))
					RV.append((0,n-2))
					RV.append((0,0))
					RV.append((1,n-1))
				elif j == 0:
					RV.append((n-1,0))
					RV.append((0,n-1))
					RV.append((0,1))
					RV.append((1,0))
				else :
					RV.append((n-1,j))
					RV.append((0,j-1))
					RV.append((0,j+1))
					RV.append((1,j))				
			elif j == n-1:
				RV.append((i-1,n-1))
				RV.append((i,n-2))
				RV.append((i,0))
				RV.append((i+1,n-1))
			elif j == 0:
				RV.append((i-1,0))
				RV.append((i,n-1))
				RV.append((i,1))
				RV.append((i+1,0))
			else:	
				RV.append((i-1,j))
				RV.append((i,j-1))
				RV.append((i,j+1))
				RV.append((i+1,j))
			return RV
			
		#Nos da las cordenadas de los casilleros que se encuentran por arriba y a la izquierda de un dado spin

		def coordEntornoInvertido(self,n):
			
			i=self.fil
			j=self.col
			RV=[]
			
			if i == n-1:
				if j == n-1:
					RV.append((n-2,n-1))
					RV.append((n-1,n-2))
				elif j == 0:
					RV.append((n-2,0))
					RV.append((n-1,n-1))
				else :
					RV.append((n-2,j))
					RV.append((n-1,j-1))
			elif i == 0:
				if j == n-1:
					RV.append((n-1,n-1))
					RV.append((0,n-2))
				elif j == 0:
					RV.append((n-1,0))
					RV.append((0,n-1))		
				else :
					RV.append((n-1,j))
					RV.append((0,j-1))			
			elif j == n-1:
				RV.append((i-1,n-1))
				RV.append((i,n-2))
			elif j == 0:
				RV.append((i-1,0))
				RV.append((i,n-1))				
								
			else:	
				RV.append((i-1,j))
				RV.append((i,j-1))				
			return RV


		#Nos da las cordenadas de los casilleros que se encuentran por debajo y a la derecha de un casillero dado 
		def coordEntornoReducido(self,n):
			
			i=self.fil
			j=self.col
			RV=[]
			
			if i == n-1:
				if j == n-1:
					RV.append((n-1,0))
					RV.append((0,n-1))
				elif j == 0:
					RV.append((n-1,1))
					RV.append((0,0))
	
				else :
					RV.append((i,j+1))
					RV.append((0,j))
			elif i == 0:
				if j == n-1:
					RV.append((0,0))
					RV.append((1,n-1))
				elif j == 0:
					RV.append((0,1))
					RV.append((1,0))
				else :
					RV.append((0,j+1))
					RV.append((1,j))				
			elif j == n-1:
				RV.append((i,0))
				RV.append((i+1,n-1))
			elif j == 0:
				RV.append((i,1))
				RV.append((i+1,0))		
								
			else:	
				RV.append((i,j+1))
				RV.append((i+1,j))
			return RV		
	
		
	#Esta funcion permite que cada vez q tipeamos 'print c' con c un casillero, nos imprima la magnetizacion q contiene
		def __str__(self):
			return str(self.magnetizacion)
			
class Red:
	#Vamos a considerar un tablero como una lista de listas de casilleros
	# ie Tablero=[[c11...c1N],...,[cN1....cNN]] donde cIJ es un casillero == 4-upla
	
	def __init__(self,n,T,B,J):
		self.tab=[]
		self.tam=n
		self.temperatura = T
		self.B = B
		self.J = J
		for i in range(n):
			F=[]
			for j in range(n):
				F.append(Particula(i,j))
			self.tab.append(F)
		self.energiaParticulas()
		self.energia = self.energiaTotal()
		self.magnetizacion = self.magnetizacionTotal()
		
	
	def montecarlo(self,x,y, betha):
			EntornoReducido = self.entornoReducido(self.tab[x][y]) # Crea una lista con las coordenadas de las particulas del entorno
			Entorno = []
			for spin in EntornoReducido:
				Entorno.append(spin)
			Entorno.append((x,y)) #Agrega la posicion (x,y)
			EntornoInvertido = self.entornoInvertido(self.tab[x][y])
			EntornoInvertido.append((x,y))
			
			#print 'El entornoReducido es:', EntornoReducido
			#print 'El entorno es:', Entorno
			#print 'El entornoInvertido es:', EntornoInvertido
			
		
		
			#Calcula energias nuevas
			energiaViejosVecinos = 0
			
			
			for spin in EntornoInvertido:
				energiaViejosVecinos = energiaViejosVecinos+ self.tab[spin[0]][spin[1]].energia 		
			#print 'La energiaViejosVecinos es:', energiaViejosVecinos
			
			#Cambio el spin de la posicion (x,y)
			self.tab[x][y].magnetizacion = self.tab[x][y].magnetizacion*(-1)
	
			#Actualiza las variables microscopicas
			for spin in EntornoInvertido:
				self.energiaInteraccion(self.tab[spin[0]][spin[1]])

			
			#Calcula energias nuevas
			energiaNuevosVecinos = 0
		
			for spin in EntornoInvertido:
				energiaNuevosVecinos = energiaNuevosVecinos+ self.tab[spin[0]][spin[1]].energia
			
			#print 'La energiaNuevosVecinos es:', energiaNuevosVecinos
			
			#Calcula el delta
			delta = energiaNuevosVecinos - energiaViejosVecinos

			#print 'El delta es:', delta
			if delta < 0: 
					self.energia = self.energia + delta
					if self.tab[x][y].magnetizacion >0:
						self.magnetizacion = self.magnetizacion + 2
					else:
						self.magnetizacion = self.magnetizacion - 2
			else:
				a = cmath.e**(-delta*betha)
				if a > random.random(): #Acepto igual
					self.energia = self.energia + delta
					if self.tab[x][y].magnetizacion >0:
						self.magnetizacion = self.magnetizacion + 2
					else:
						self.magnetizacion = self.magnetizacion - 2
					#print 'Hubo cambio'
				else: 
					#Cambio el spin de la posicion (x,y)
					self.tab[x][y].magnetizacion = self.tab[x][y].magnetizacion*(-1)
			
					#Actualiza las variables microscopicas
					for spin in EntornoInvertido:
						self.energiaInteraccion(self.tab[spin[0]][spin[1]])
					#print 'No hubo cambio'
	
	
	#Energia de las interacciones derecha y abajo de las particula de la red

	def energiaParticulas(self):
		n= self.tam
		for i in range(n):
			F=[]
			for j in range(n):
				self.energiaInteraccion(self.tab[i][j])
			self.tab.append(F)
		
		
	
	
	#Calcula la energia de la interaccion a la derecha y abajo de una particula
	
	def energiaInteraccion(self,c):
		J  = self.J
		energia = 0
		
		E = self.entornoReducido(self.tab[c.fil][c.col])
		for casillero in E:
			energia = energia - J*self.tab[casillero[0]][casillero[1]].magnetizacion*c.magnetizacion
		c.energia = energia 
	
		
	#Nos devuelve los casilleros que se encuentran a la derecha y abajo del spin c en la red
	def entornoReducido(self,c):
		n = self.tam 
		P=c.coordEntornoReducido(n)
		return P
		
		
	def entornoInvertido(self,c):
		n = self.tam 
		P=c.coordEntornoInvertido(n)
		return P

		
	# Variables macroscopicas	
	
	def energiaTotal(self):
		energiaTotal = 0
		for x in range(0,self.tam):
			for y in range(0,self.tam):
				energiaTotal = energiaTotal + self.tab[x][y].energia
		
		return energiaTotal
		
		
		
	def magnetizacionTotal(self):
		magnetizacionTotal = 0
		for x in range(0,self.tam):
			for y in range(0,self.tam):
				magnetizacionTotal = magnetizacionTotal + self.tab[x][y].magnetizacion
		return magnetizacionTotal
	
		
	
	
	#Definimos estas dos funciones para imprimir el tablero de juego y para corroborar que se armo como queremos
		
	def imprimir(self):
		for x in range(0,self.tam):
			for y in range(0,self.tam):
				if self.tab[x][y].magnetizacion == 1:
						print '',self.tab[x][y],
				else:
						print self.tab[x][y],
			print
			
	def imprimirEnergias(self):
		print
		for x in range(0,self.tam):
			for y in range(0,self.tam):
				if self.tab[x][y].energia >= 0:
						print '',self.tab[x][y].energia,
				else:
						print self.tab[x][y].energia,
			print
	

	
	
	
	
	
	
	
	
	
	
