import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

if __name__ == "__main__":
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    
    if longitud < 1:
        print("La longitud de la contraseña debe ser al menos 1.")
    else:
        contrasena_generada = generar_contrasena(longitud)
        print(f"Contraseña generada: {contrasena_generada}")
