def Fibonacci(z):
	if (z==0 or z==1):
		return z
	else:
		a=0
		b=1
		c=1
		for i in range (1,z):
			c=a+b
			a=b
			b=c
	return c
z=int(input("Ingresa el numero a ser Fibonacciado: "))
fib=Fibonacci(z)
print("El Fibonacci de: "+str(z)+" Es: "+str(fib))

