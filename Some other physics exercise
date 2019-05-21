from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
import glob

a='27'

def sacarota(a):
	a[524]= (a[523]+a[525])/2# Esto es porque el pixel correspondiente a 564.11 no funciona correctamente


def crearDiccionario(txt):
	b = {}
	j = 0
	referencias={'pepe':'P1 y P2 en s','pepa':'P1 en s y P2 en p',
	'pape':'P1 en p y P2 en s', 'papa':'P1 y P2 en p','pa':'P1 en p',
	'pe':'P1 en s', 'rui1': 'ruido con polarizador p2', 'rui2': 'ruido sin polarizador p2'}
	for j in txt:
		if referencias.has_key(j[0:4]):
			data = genfromtxt(j, skip_header = 17, skip_footer = 1)
			b[j]=referencias[j[0:4]], data
		elif referencias.has_key(j[0:2]):
			data = genfromtxt(j, skip_header = 17, skip_footer = 1)
			b[j]=referencias[j[0:2]], data
	return b

def ej3(patron, cetonia, ruido):
	#Calcula los errores porcentuales
	
	lamvda = patron['pe3355.txt'][1][:,0]
	p1 = patron['pepa3355.txt'][1][:,1]
	sacarota(p1) # Esto es porque el pixel correspondiente a 564.11 no funciona correctamente
	p2 = patron['pepe3355.txt'][1][:,1]
	sacarota(p2)
	p3 = patron['papa3355.txt'][1][:,1]
	sacarota(p3)
	p4 = patron['pape3355.txt'][1][:,1]
	sacarota(p4)
	rp = ruido['rui1.txt'][1][:,1]#Ruido para P1 en p
	sacarota(rp)
	rs = ruido['rui2.txt'][1][:,1]#Ruido para P1 en s
	sacarota(rs)
			
	pe = ((p1-rs)/(p2+p1-2*rs)) *100
	pa = ((p4-rp)/(p3+p4-2*rp)) *100
	pe = pe*np.sign(pe)
	pa = pa*np.sign(pa)
	return pa, pe
	
def graficaej3(patron, cetonia, ruido, pa, pe):
	#Grafica los errores porcentuales

	lamvda = patron['pe3355.txt'][1][:,0]
	plt.plot(lamvda, pe, label = 'Error de P1 en s')
	plt.plot(lamvda, pa, label = 'Error de P1 en p')
	plt.axis([350, 800, -10, 100])
	plt.xlabel('Longitud de onda (nm)')
	plt.ylabel('Cruzado/paralelos (%)')
	plt.title('Cruzado/paralelos (%) vs longitud de onda (nm)')
	plt.legend(loc=1)

	plt.grid(True)
	plt.savefig('errorporcentual'+'.pdf')

	plt.show()


def ej4(patron, cetonia, ruido, pa, pe):
	#Grafica la intensidad 
	
	lamvda = patron['pe3355.txt'][1][:,0]
		
	perp = patron['pe3355.txt'][1][:,1]
	sacarota(perp)
	para = patron['pa3355.txt'][1][:,1]
	sacarota(para)
	
	
	perpmax = perp + perp*pe/100
	perpmin = perp - perp*pe/100
	plt.plot(lamvda, perp, label = 'P1 en s')
	plt.plot(lamvda, perpmax, label = 'P1 en s max')
	plt.plot(lamvda, perpmin, label = 'P1 en s min')
	paramax = para + para*pa/100
	paramin = para - para*pa/100
	plt.plot(lamvda, para, label = 'P1 en p')
	plt.plot(lamvda, paramax, label = 'P1 en p max')
	plt.plot(lamvda, paramin, label = 'P1 en p min')



	plt.axis([350, 800, 0, 65000])
	plt.xlabel('Longitud de onda (nm)')
	plt.ylabel('Intensidad (cuentas)')
	plt.title('Intensidad (cuentas) vs longitud de onda (nm)')
	plt.legend(loc=2)

	plt.grid(True)

	plt.show()

def ej5(patron, cetonia, ruido, pa, pe,a):
	lamvda = patron['pe3355.txt'][1][:,0]
	perp = patron['pe3355.txt'][1][:,1]
	sacarota(perp)
	para = patron['pa3355.txt'][1][:,1]
	sacarota(para)
	rp= ruido['rui1.txt'][1][:,1]
	sacarota(rp) # Esto es porque el pixel correspondiente a 564.11 no funciona correctamente
	rs= ruido['rui2.txt'][1][:,1]
	sacarota(rs)
	s1 = cetonia['pepa.txt'][1][:,1]
	sacarota(s1) 
	s2 = cetonia['pepe.txt'][1][:,1]
	sacarota(s2) 
	s3 = cetonia['papa.txt'][1][:,1]
	sacarota(s3) 	
	s4 = cetonia['pape.txt'][1][:,1]
	sacarota(s4) 
	graficaperppara(lamvda, perp,rs,s1,a)
	graficaperpperp(lamvda, perp,rs,s2,a)
	graficaparapara(lamvda, para,rp,s3,a)
	graficaparaperp(lamvda, para,rp,s4,a)
	


def graficaperppara(lamvda, perp,rs,s1,a):

	
	#Grafica perppara
	reflec1 = (s1-rs)/(perp-rs)*100
	reflec1max = reflec1+reflec1*pe*0.02
	reflec1min = reflec1-reflec1*pe*0.02
	
	
	
	plt.plot(lamvda, reflec1, label = 's: cross')
	plt.plot(lamvda, reflec1max, label = 's: cross max')
	plt.plot(lamvda, reflec1min, label = 's: cross min')
	
		#Propiedades del grafico
	plt.axis([475, 800, -10, 110])
	plt.xlabel('Longitud de onda (nm)')
	plt.ylabel('Reflectancia (%)')
	plt.title('Reflectancia (%) vs longitud de onda (nm)')
	plt.legend(loc=1)

	plt.grid(True)
	plt.savefig('sp'+a+'.pdf')
	plt.close()

def graficaperpperp(lamvda, perp,rs,s2,a):

	
	#Grafica perpperp
	reflec2 = (s2-rs)/(perp-rs)*100
	reflec2max = reflec2+reflec2*pe*0.02
	reflec2min = reflec2-reflec2*pe*0.02
	
	
	
	plt.plot(lamvda, reflec2, label = 's: co')
	plt.plot(lamvda, reflec2max, label = 's: co max')
	plt.plot(lamvda, reflec2min, label = 's: co min')

		#Propiedades del grafico
	plt.axis([475, 800, -10, 110])
	plt.xlabel('Longitud de onda (nm)')
	plt.ylabel('Reflectancia (%)')
	plt.title('Reflectancia (%) vs longitud de onda (nm)')
	plt.legend(loc=1)

	plt.grid(True)
	plt.savefig('ss'+a+'.pdf')

	plt.close()















	
def graficaparapara(lamvda, para,rp,s3,a):
	
	
	#Grafica para
	reflec3 = (s3-rp)/(para-rp)*100
	reflec3max = reflec3+reflec3*pa*0.02
	reflec3min = reflec3-reflec3*pa*0.02
	plt.plot(lamvda, reflec3, label = 'p: co')
	plt.plot(lamvda, reflec3max, label = 'p: co max')
	plt.plot(lamvda, reflec3min, label = 'p: co min')
	
	#Propiedades del grafico
	plt.axis([475, 800, -10, 110])
	plt.xlabel('Longitud de onda (nm)')
	plt.ylabel('Reflectancia (%)')
	plt.title('Reflectancia (%) vs longitud de onda (nm)')
	plt.legend(loc=1)

	plt.grid(True)
	plt.savefig('pp'+a+'.pdf')
	plt.close()
	

def graficaparaperp(lamvda, para,rp,s4,a):	
	reflec4 = (s4-rp)/(para-rp)*100
	reflec4max = reflec4+reflec4*pa*0.02
	reflec4min = reflec4-reflec4*pa*0.02
	
	plt.plot(lamvda, reflec4, label = 'p: cross')
	plt.plot(lamvda, reflec4max, label = 'p: cross max')
	plt.plot(lamvda, reflec4min, label = 'p: cross min')

	
	#Propiedades del grafico
	plt.axis([475, 800, -10, 110])
	plt.xlabel('Longitud de onda (nm)')
	plt.ylabel('Reflectancia (%)')
	plt.title('Reflectancia (%) vs longitud de onda (nm)')
	plt.legend(loc=1)

	plt.grid(True)
	plt.savefig('ps'+a+'.pdf')



txt = glob.glob('*.txt')
patron = glob.glob('*3355.txt')
ruido = glob.glob('rui*')
patron = set(patron)
ruido = set(ruido)
txt = set(txt)
cetonia = txt.difference(patron.union(ruido))
cetonia = crearDiccionario(cetonia)
ruido = crearDiccionario(ruido)
patron = crearDiccionario(patron)
'''
#----EJ 1 ------
ej1(patron, cetonia, ruido)
'''
'''
#----EJ 2 ------
ej2(patron, cetonia, ruido)
'''

#--------EJ 3----------------
#----Devuelve el error para cada longitud de onda para una luz incidente perpendicular (Pe) al plano de incidencia
#-- y una paralela (Pa) a este.

pa, pe = ej3(patron, cetonia, ruido)
graficaej3(patron,cetonia,ruido,pa,pe)


#-------Ej 4---------------
#Grafica intensidad del patron con el ruido en las dos configuraciones. Se necesita Ej3
ej4(patron, cetonia, ruido, pa, pe)

#-------Ej 5---------------
#Grafica reflectancia del cetonia  con error. Se necesita Ej3
ej5(patron, cetonia, ruido, pa, pe,a)








