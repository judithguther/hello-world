import random
import string

char_pwd = int(input())
contrasena_creada = ""
# caracteres = ['1','2','3','4','5','6','7','8','9','0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
caracteres = string.ascii_letters + string.digits + string.punctuation
for x in range(char_pwd):
    contrasena_creada = contrasena_creada + (random.choice(caracteres))
print(contrasena_creada)