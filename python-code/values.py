import os
import nltk
import pandas as pd

# Ruta del directorio que contiene los archivos de texto
corpus_directory = 'directorio'

# Inicializar el tokenizador de NLTK para dividir el texto en palabras
tokenizer = nltk.RegexpTokenizer(r'\b\w+\b')

# Crear listas para almacenar los resultados por archivo
results_list = []

# Recorrer los archivos en el directorio
for filename in os.listdir(corpus_directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(corpus_directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            tokens = tokenizer.tokenize(text.lower())  # Tokenizar y convertir a minúsculas
            num_tokens = len(tokens)
            num_types = len(set(tokens))
            ttr_percentage = (num_types / num_tokens) * 100
            results_list.append([filename, num_tokens, num_types, ttr_percentage])

# Crear una tabla con los resultados
results_df = pd.DataFrame(results_list, columns=['Archivo', 'Tokens', 'Types', 'Type-Token Ratio (%)'])

# Imprimir la tabla de resultados
print(results_df)
