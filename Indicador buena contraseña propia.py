contrasena = input()
contador = 0

while True:
    if (len(contrasena) < 8 or len(contrasena) > 16):
        contador = int(contador) + 1
        break
    elif contrasena.islower() == True:
        contador = int(contador) + 1
        break
    elif any(chr.isdigit() for chr in contrasena) == False:
        # usamos any para ver si en alguno de los caracteres del string se cumple el bucle for. de ser así, nos devolvería True. 
        # el bucle for en este caso busca que haya algún dígito (de ahí el uso de .isdigit) en los caracteres de la variable contraseña. 
        # si hubiera, nos devolvería True, por lo que esta condición elif no se triggerearía. 
        # si no hubiera dígitos, el any sería False, coincidiendo con la condición elif y triggereándola.
        contador = int(contador) + 1
        break
    else:
        # importante romper el bucle si queremos que nos lleve al caso de que no tengamos ningun contador añadido, esto es, que nuestra contraseña sea buena.
        break
if contador == 0:
    print("Buena contraseña.")
elif contador != 0:
    print("Contraseña débil o muy larga.")