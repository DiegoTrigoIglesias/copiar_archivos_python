#METODO FACIL
Archivo_leido=open("datos.txt","r")#leemos un archivo linea a linea (R de lectura) y el nombre del archivo  
contenido=Archivo_leido.read() #cogemos su contenido 
Archivo_Final=open("archivo_final.txt","w")#creamos el archivo donde se copiaran los datos (W de escritura )
Archivo_Final.write(contenido)#escribimos el contenido en el archivo final 


#OTRO METODO
def copiaArchivo(archivo_entrada, archivo_salida):
    fileInput = open(archivo_entrada, "r")# leemos un archivo linea a linea (R de lectura) y el nombre del archivo
    fileContent = fileInput.read()  # cogemos su contenido
    fileOutput = open(archivo_salida, "w") # creamos el archivo donde se copiaran los datos (W de escritura )
    fileOutput.write(fileContent)  # escribimos el contenido en el archivo final

copiaArchivo("texto.txt", "texto_copia.txt")