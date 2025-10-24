#semilla inicial
semilla = 5735

cantidad = 3

for i in range(cantidad):
    cuadrado = semilla ** 2      
    texto = str(cuadrado).zfill(8)   
    medio = texto[2:6]               
    semilla = int(medio)             
    numero = semilla / 10000         
    print(numero)
