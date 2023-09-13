import os
import spacy

# Cargar el modelo de spaCy para inglés (o la lengua del corpus)
sp = spacy.load('en_core_web_sm')

# Pega aquí el directorio con las novelas originales y el directorio donde se guardarán las novelas lematizadas
dir_entrada = "directorio1"
dir_salida = "directorio2"

# Bucle para recorrer los textos del directorio original
for txt in os.listdir(dir_entrada):
    with open(os.path.join(dir_entrada, txt), "r", encoding="utf-8") as archivo:
        # Leer el archivo de entrada
        contenido = archivo.read().lower()
        
        # Lematizar el contenido del archivo
        lemas = []
        doc = sp(contenido)
        for token in doc:
            lemas.append(token.lemma_)
        
        # Unir los lemas en una cadena de texto
        lemas_str = " ".join(lemas)
        
        # Guardar la cadena de lemas en el archivo de salida
        with open(os.path.join(dir_salida, txt), "w", encoding="utf-8") as archivo2:
            archivo2.write(lemas_str)
