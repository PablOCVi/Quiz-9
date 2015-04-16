def distancia(x,y,z,w):
	r=(-x+z)**2
	s=(-y+w)**2
	import math
	q= math.sqrt(r+s)
	return q
x=int(input("Ingresa el valor de x del primer punto: "))
y=int(input("Ingresa el valor de y del primer punto: "))
z=int(input("Ingresa el valor de x del segundo punto: "))
w=int(input("Ingresa el valor de y del segundo punto: "))
h=distancia(x,y,z,w)
print("La distancia es: "+str(h))
