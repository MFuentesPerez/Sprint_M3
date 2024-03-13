import random
import string

# Lista de nombres de usuarios
nombres_usuarios = ["Luis", "Maria", "Miguel", "José", "Andres",
                    "Sofía", "Luisa", "Ana", "Eduardo", "Mario"]


# Función para generar una contraseña aleatoria
def generar_contraseña():
    caracteres = string.ascii_letters + string.digits  # Agrega letras y numeros
    contraseña = ''.join(random.choice(caracteres) for i in range(8))
    return contraseña

# Crear cuentas para cada usuario
cuentas_usuarios = {}
for nombre in nombres_usuarios:
    contraseña = generar_contraseña()
    cuenta = {'contraseña': contraseña}
    cuentas_usuarios[nombre] = cuenta # Asignacion de cuenta al usuario

# Pedir número telefónico para cada cuenta
while True:
    todas_tienen_numero = True #Flag de control
    for nombre, cuenta in cuentas_usuarios.items():
        if 'telefono' not in cuenta: # Verifica key telefono en cada cuenta de usuario para agregarla si no existe
            todas_tienen_numero = False
            numero_telefono = input(f"Ingrese el número telefónico para {nombre}: ")
            if numero_telefono.isdigit() and len(numero_telefono) == 8: # Control de que el valor ingresado sea numerico de 8 caracteres
                cuenta['telefono'] = numero_telefono
            else:
                print("El número telefónico debe tener 8 dígitos numéricos.")
    
    if todas_tienen_numero:
        break

# Imprimir cuentas de usuarios con sus respectivos números telefónicos
print("\nCuentas de usuarios con números telefónicos:")
for nombre, cuenta in cuentas_usuarios.items():
    print(f"Usuario: {nombre}, Contraseña: {cuenta.get('contraseña')}, Número telefónico: {cuenta.get('telefono')}") 
