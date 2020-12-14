from flask import Flask, request
import requests

app = Flask(__name__)

url = "https://iglesiapeniel.website/api/pantalla/5fc714a9828833e8d6c21719/"


def enviarPeticion(caracter):
    requests.get(url+caracter)


@app.route('/1')
def uno():
    enviarPeticion("1")
    return {"mensaje": "Enviado"}


@app.route('/2')
def dos():
    enviarPeticion("2")
    return {"mensaje": "Enviado"}


@app.route('/3')
def tres():
    enviarPeticion("3")
    return {"mensaje": "Enviado"}


@app.route('/4')
def cuatro():
    enviarPeticion("4")
    return {"mensaje": "Enviado"}


@app.route('/5')
def cinco():
    enviarPeticion("5")
    return {"mensaje": "Enviado"}


@app.route('/6')
def seis():
    enviarPeticion("6")
    return {"mensaje": "Enviado"}


@app.route('/7')
def siete():
    enviarPeticion("7")
    return {"mensaje": "Enviado"}


@app.route('/8')
def ocho():
    enviarPeticion("8")
    return {"mensaje": "Enviado"}


@app.route('/9')
def nueve():
    enviarPeticion("9")
    return {"mensaje": "Enviado"}


@app.route('/#')
def numeral():
    enviarPeticion("L")
    return {"mensaje": "Enviado"}


@app.route('/*')
def asterisko():
    enviarPeticion("L")
    return {"mensaje": "Enviado"}


@app.route('/L')
def ele():
    enviarPeticion("L")
    return {"mensaje": "Enviado"}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
