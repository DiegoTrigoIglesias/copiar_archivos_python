def copiaArchivo(nameInput, nameOutput):
    """
    Lee un archivo entero y lo copia en
    @type  nameInput: String
    @param nameInput: Archivo que vamos a leer
    @type  nameOutput: number
    @param bnameOutput: Archivo donde vamos a escribir
    """
    fileInput = open(nameInput, "r")# leemos un archivo linea a linea (R de lectura) y el nombre del archivo
    fileContent = fileInput.read()  # cogemos su contenido
    fileOutput = open(nameOutput, "w") # creamos el archivo donde se copiaran los datos (W de escritura )
    fileOutput.write(fileContent)  # escribimos el contenido en el archivo final

try:
    copiaArchivo("texto.txt", "texto_copy.txt")
    print("Hecho")
except:
    print("Error durante el copiado")