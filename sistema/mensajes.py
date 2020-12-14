import requests
import serial
from time import sleep
from threading import Thread

ser = serial.Serial("/dev/ttyS0", 9600)  # Open port with baud rate

while True:
    response = requests.get("https://iglesiapeniel.website/api/eventos")
    eventos = response.json()["eventos"]
    response = requests.get("https://iglesiapeniel.website/api/usuarios")
    usuarios = response.json()["usuarios"]
    print(usuarios)

    for evento in eventos:
        if "publicar" in evento:
            if evento["publicar"] == True:
                for usuario in usuarios:
                    print("Enviando...")
                    ser.write("AT+CMGF=1\r\n")
                    sleep(0.5)
                    ser.write("AT+CMGS=\"+593" +
                              usuario["telefono"][1:].encode()+"\"\r\n")
                    sleep(1.5)
                    ser.write(evento["nombre"].encode()+chr(26))
                requests.put(
                    "https://iglesiapeniel.website/api/eventos/"+evento["_id"]+"/nopublicar")
    sleep(3)
