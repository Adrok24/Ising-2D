from Red import  Particula, Red
from random import randint as rnd
from random import random as random
from numpy import mean as mean
from numpy import std as std
from numpy import linspace as ln
import time
import cmath
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


B = 0
J = 1

iteraciones = 200
n=32
ENERGIAS = []
ENERGIASPORSITIO = []
MAGNETIZACIONESPORSITIO = []
MAGNETIZACIONES = []
TEMPERATURAS = []
TEMPERATURAS.extend(ln(0.1,10.1, num = 20))



for temperatura in TEMPERATURAS:
	Spines=Red(n, temperatura, B, J)
	betha = 1/temperatura
	energias =[]
	magnetizaciones = []
	for k in xrange(0,iteraciones):
	#Recorro spines. 1 "paso" es recorrer todos.
		for i in xrange(0,n):
			for j in xrange(0,n):
	## Da vuelta un spin o no siguiendo el criterio montecarlo y calcula la energia y la magnetizacion total.
				Spines.montecarlo(i,j, betha)
				energias.append(Spines.energia) 
				magnetizaciones.append(Spines.magnetizacion)
	
	with open('termalizacion'+str(temperatura)+'.txt', 'w') as f:
		for f1, f2 in zip(energias, magnetizaciones):
			print >> f, f1, f2	
	plt.plot(energias,'b.', label = 'Energia')
	plt.xlabel('Iteraciones')
	plt.ylabel('Energia')
	plt.title('Energia por sitio vs Iteraciones')
	plt.legend(loc=1)
	plt.grid(True)
	plt.savefig('energia'+str(temperatura)+'.pdf')
	plt.close()
	print 'Iteracion 1'

