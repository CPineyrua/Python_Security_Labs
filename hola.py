nombre = input("¿Cuál es tu nombre? ")
import random

print(f"Hola {nombre}, bienvenido a Cursor 😊")
numero_secreto = random.randint(1, 10)
intento = int(input("Estoy pensando en un número del 1 al 10. ¿Puedes adivinar cuál es? "))

if intento == numero_secreto:
    print("¡Felicidades! ¡Adivinaste el número!")
else:
    print(f"No adivinaste. El número era {numero_secreto}. ¡Suerte la próxima vez!")
    