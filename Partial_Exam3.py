#Pablo Enrique Cárdenas Viera
#3 Superpower
def superpower(a,n):
	ans=a
	for i in range (1,n):
		ans=ans*a
	return ans
a=int(input("Ingresa el primer valor: "))
n=int(input("Ingresa el segundo valor:"))
sp=superpower(a,n)

print("El resultado de: "+str(a)+" Multiplicado consigo mismo: "+str(n)+" veces.")
print("Es: "+str(sp))

