a = 5
m = 16
x0 = 7

n = 5

numeros = []

x = x0
for i in range(n):
    x = (a * x) % m
    numeros.append(x)
    
    
    print("numeros generados:")
    print(numeros)
    