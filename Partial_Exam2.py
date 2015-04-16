def triangulo(n):
	x="T"
	z=1
	while(n>z):
		x="T"
		
		print(x*z)
		z=z+1
	print(x*n)
	z=n-1
	while(z>1):
		x="T"
		
		print(x*z)
		z=z-1
	print(x)

n=int(input("Ingrese el tamano del triangulo: "))
tri=triangulo(n)


