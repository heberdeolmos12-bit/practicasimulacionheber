#parametros 
a = 5
c = 3
m = 5
x0 = 7

n = 6

numeros = []

x = x0
for i in range(n):
    x = (a * x + c) % m
    numeros.append(x)
    
    print("numeros generados:")
    print(numeros)
    99