from chunks import Archivo

if __name__=="__main__":
    a1=Archivo("prueba.mp3","./","./")
    print(a1.rutaDestino)
    print(a1.nombre)
    

    print(a1.envio("prueba.mp3","./","./"))




