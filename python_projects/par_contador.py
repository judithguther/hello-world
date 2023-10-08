numero = 1
contador = 0
while True:
    numero = int(input())
    resto = numero % 2
    if numero == 0:
        break
    if resto == 0:
        print("Par")
        contador = contador +1
    elif resto != 0:
        print("Impar")
print("La cantidad de números pares es " + str(contador))




