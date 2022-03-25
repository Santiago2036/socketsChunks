import os
from time import sleep


class Archivo:
    
    def __init__(self,nombre,rutaOrigen,rutaDestino):
        self.nombre=nombre
        self.rutaOrigen=rutaOrigen
        self.rutaDestino=rutaDestino
        self.__cache=b''
        self.__version=0
        self.banderaFin=0

    def __str__(self):
        return self.nombre
    
    def __str__(self):
        return self.rutaOrigen
    
    def __str__(self):
        return self.rutaDestino


    def union(self,nombre,data):####solo falta la union

        #########################################
        print("Estamos en union")
        ##########################################
        with open('Archivo_final.mp3','ab')as filee:
            filee.write(data)
            print(data)
            sleep(10)
        
        


        return "UNION REALIZADA!!"

    def chunk(self,nombre,data,rutaDestino):

        self.nombre=nombre
        self.__version+=1
        self.nombre=str(self.__version)+self.nombre
    
        self.__cache=self.__cache+data
        self.union(self.nombre,data)
        """
        with open(self.nombre,'wb+') as filee:
                filee.write(self.__cache)
                print("vAMOS AS UNION")
                self.union(self.nombre,data)
        """

     
        return "CHUNKS ENVIADOS PARA UNION" 

    
    def envio(self,nombre,rutaOrigen,rutaDestino):
        CHUNK_SIZE = 1000000
        size = CHUNK_SIZE
        total= 0
        parts = 0
        fileName=self.nombre
        filee= open(fileName, 'rb')
        while (size >= CHUNK_SIZE):
        
            offset = int(total)
            chunksz = int(CHUNK_SIZE)
            # Leer data segun el tamaño del chunk
            filee.seek(offset, os.SEEK_SET)
            dataInBytes = filee.read(chunksz)
            #print(dataInBytes)
            self.chunk(fileName,dataInBytes,self.rutaDestino)
            if(len(dataInBytes) == 0):
                self.banderaFin=1
                break

            parts += 1
            # leyendo el tamaño en bytes del chunk y guardando en variable
            size = len(dataInBytes)
            # Agregando el tamaño en bytes a la variable TOTAL
            total += size


        filee.close()

        return "bien"#self.chunk(self.nombre,data)










        