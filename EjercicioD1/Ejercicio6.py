import random
import string

def generar_contrasena(longitud):
    if longitud < 4:
        print("La longitud de la contraseña debe ser al menos 4 caracteres.")
        return None
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = []

    contrasena.append(random.choice(string.ascii_lowercase))
    contrasena.append(random.choice(string.ascii_uppercase))
    contrasena.append(random.choice(string.digits))
    contrasena.append(random.choice(string.punctuation))

    contrasena += random.choices(caracteres, k=longitud-4)
    
    random.shuffle(contrasena)
    
    return ''.join(contrasena)

def main():
    try:
        longitud = int(input("Introduce la longitud de la contraseña: "))
        contrasena = generar_contrasena(longitud)
        if contrasena:
            print(f"Contraseña generada: {contrasena}")
    except ValueError:
        print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()
