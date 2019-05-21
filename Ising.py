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




energias=[]
magnetizaciones =[]
B = 0
J = 1

termalizar = 50
iteraciones = 500
n=32
ENERGIAS = []
ENERGIASPORSITIO = []
MAGNETIZACIONESPORSITIO = []
MAGNETIZACIONES = []
SIGMASE =[]
SIGMASM =[]
CV = []
SUSCEPTIBILIDAD = []
TEMPERATURAS = []
TEMPERATURAS.extend(ln(0.1,1.0, num = 10,endpoint = False))
TEMPERATURAS.extend(ln(1.0,4.0, num = 101,endpoint = False))
TEMPERATURAS.extend(ln(4.0,10.1, num = 101))



Spines=Red(n, TEMPERATURAS[0], B, J)
betha = 1/TEMPERATURAS[0]


# Termalizar.
for k in xrange(0,termalizar):
#Recorro spines. 1 "paso" es recorrer todos.
	for i in xrange(0,n):
		for j in xrange(0,n):
## Dar vuelta un spin
			Spines.montecarlo(i,j, betha)







for temperatura in TEMPERATURAS:
	
	
	t= time.time()

	betha = 1/temperatura


	energias = []
	magnetizaciones = []
		
	
	for k in xrange(0,iteraciones):
	#Recorro spines. 1 "paso" es recorrer todos.
		for i in xrange(0,n):
			for j in xrange(0,n):
	## Dar vuelta un spin
				Spines.montecarlo(i,j, betha)
		#Cada vez que recorre toda la red agrega la energia y la magnetizacion medida		
		energias.append(Spines.energia) 
		magnetizaciones.append(Spines.magnetizacion)
	
	
	#Calcula la energia media de todas las energias que fue midiendo para esa temperatura 
	energiamedia = mean(energias)
	magnetizacionmedia = mean(magnetizaciones)

	
	
	ENERGIAS.append(energiamedia)
	ENERGIASPORSITIO.append(energiamedia/(n*n))
	sigmaE = std(energias)
	SIGMASE.append(sigmaE)
		
	MAGNETIZACIONES.append(magnetizacionmedia)
	MAGNETIZACIONESPORSITIO.append(magnetizacionmedia/(n*n))
	sigmaM = std(magnetizaciones)
	SIGMASM.append(sigmaM)
	
	susceptibilidad = temperatura*(sigmaM*betha/n)**2
	cv = (sigmaE*betha/n)**2
	
	CV.append(cv)
	SUSCEPTIBILIDAD.append(susceptibilidad)
	elapsed = time.time() - t
	print 'La energia total es:', energiamedia
	print 'La energia por particula es:', energiamedia/(n*n)
	print 'La magnetizacion por particula es:', magnetizacionmedia/(n*n)
	print 'La magnetizacion total es:', magnetizacionmedia
	print 'Si las iteraciones son:', iteraciones, ', el tiempo es', elapsed
	print 'Temperatura es:', temperatura
	print 'El CV es:', cv
	print 'La susceptibilidad es:', susceptibilidad



with open('resultados.txt', 'w') as f:
    for f1, f2, f3, f4, f5 in zip(TEMPERATURAS, ENERGIASPORSITIO, MAGNETIZACIONESPORSITIO , CV, SUSCEPTIBILIDAD):
        print >> f, f1, f2, f3, f4, f5	


	
plt.plot(TEMPERATURAS, ENERGIASPORSITIO,'b.', label = 'Energia')
plt.xlabel('Temperatura')
plt.ylabel('Energia')
plt.title('Energia por sitio vs T')
plt.legend(loc=1)
plt.grid(True)
plt.savefig('energia.pdf')
plt.show()

plt.plot(TEMPERATURAS, MAGNETIZACIONESPORSITIO,'y.', label = 'Magnetizacion')
plt.xlabel('Temperatura')
plt.ylabel('Magnetizacion')
plt.title('Magnetizacion por sitio vs T')
plt.legend(loc=1)
plt.grid(True)
plt.savefig('magnetizacion.pdf')
plt.show()



plt.plot(TEMPERATURAS, CV,'r.', label = ' CV' )
plt.xlabel('Temperatura')
plt.ylabel('CV')
plt.title('CV vs T')
plt.legend(loc=1)
plt.grid(True)
plt.savefig('CV.pdf')
plt.show()


plt.plot(TEMPERATURAS, SUSCEPTIBILIDAD,'g.', label = ' Susceptibilidad' )
plt.xlabel('Temperatura')
plt.ylabel('Susceptibilidad')
plt.title('Susceptibilidad vs T')
plt.legend(loc=1)
plt.grid(True)
plt.savefig('Susceptibilidad.pdf')
plt.show()
















	
	

