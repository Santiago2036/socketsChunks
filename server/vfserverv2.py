import zmq
import sys
import json
import codecs
import os
import shutil
from time import sleep

context = zmq.Context()
clients = context.socket(zmq.REP)
clients.bind("tcp://*:9999")


while True:
    print("Esperando peticion...")

    datos, nombre, data = clients.recv_multipart()
    diccionario = json.loads(datos)

    if diccionario["accion"] == "upload":
        nombre = nombre.decode("utf-8")
        with open(nombre, "ab") as filee:
            filee.write(data)
            print(data)

    clients.send_string("LISTO!!")
