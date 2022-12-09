import pyautogui as spam
import time

mensaje = input("Ingrese el mensaje que quiere enviar ")
numeroMensajes = input("Numero de veces para enviar el mensaje")


#enviar muchos mensajes a cualquier red social
i = 0
time.sleep(5)
while i < int(numeroMensajes):
    spam.typewrite(mensaje)
    spam.press("enter")
    i += 1
    print("enviado")


