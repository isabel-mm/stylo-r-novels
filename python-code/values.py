import os
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Directorio donde se aloja tu corpus
directorio = 'tudirectorio'

# Lista para almacenar los resultados de cada texto
resultados = []

# Recorre los archivos en el directorio
for filename in os.listdir(directorio):
    if filename.endswith('.txt'):  # Para solo procesar archivos de texto
        with open(os.path.join(directorio, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            tokens = word_tokenize(text)
            total_tokens = len(tokens)
            types = set(tokens)
            total_types = len(types)
            ttr = (total_types / total_tokens) * 100  # TTR como porcentaje

            # Agrega los resultados a la lista
            resultados.append([filename, total_tokens, total_types, f"{ttr:.2f}%"])

# Imprime la tabla en formato Markdown
print("| Archivo | Total de Tokens | Total de Types | Type-Token Ratio (TTR) |")
print("|---------|-----------------|---------------|-------------------------|")

for resultado in resultados:
    print(f"| {resultado[0]} | {resultado[1]} | {resultado[2]} | {resultado[3]} |")
