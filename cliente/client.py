import zmq
import json
import os

#############################CREACION DEL SOCKET###########################################################
context = zmq.Context()

server = context.socket(zmq.REQ)
server.connect("tcp://localhost:9999")
##############################FUNCIONES####################################################################
def Envio(nombre, rutaOrigen, envio):
    CHUNK_SIZE = 5
    size = CHUNK_SIZE
    total = 0
    parts = 0
    fileName = nombre
    filee = open(fileName, "rb")
    while size >= CHUNK_SIZE:

        offset = int(total)
        chunksz = int(CHUNK_SIZE)
        # Leer data segun el tamaño del chunk
        filee.seek(offset, os.SEEK_SET)
        dataInBytes = filee.read(chunksz)
        # print(dataInBytes)
        chunk(fileName, dataInBytes, envio)
        if len(dataInBytes) == 0:
            banderaFin = 1
            break

        parts += 1
        # leyendo el tamaño en bytes del chunk y guardando en variable
        size = len(dataInBytes)
        # Agregando el tamaño en bytes a la variable TOTAL
        total += size

    filee.close()

    return "bien"  # self.chunk(self.nombre,data)


def chunk(nombre, data, envio):
    new_envio = json.dumps(envio)

    server.send_multipart([new_envio.encode("utf-8"), filename.encode("utf-8"), data])
    recibe = server.recv_string()
    return "CHUNKS ENVIADOS PARA UNION"




##########ENTRADA DEL PROGRAMA####################
filename = "prueba.txt"
accion = input("Ingrese Accion")
envio = {"accion": accion, "uparchivo": filename}

if accion == "upload":
    Envio(filename, "./", envio)
