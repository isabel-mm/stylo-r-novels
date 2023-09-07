# Este código imprime una tabla con el número de tokens y número de types del corpus. También calcula el type-token ratio.

import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Pega aquí el directorio donde se encuentra tu corpus
corpus_directory = 'C:/tudirectorio'

# Función para contar tokens, tipos y calcular el type-token ratio
def count_tokens_types_ttr(text):
    tokens = word_tokenize(text, language='english')
    types = set(tokens)
    ttr = len(types) / len(tokens)
    return len(tokens), len(types), ttr

# Bucle para iterar sobre los archivos en el directorio
for filename in os.listdir(corpus_directory):
    if filename.endswith('.txt'):
        with open(os.path.join(corpus_directory, filename), 'r', encoding='utf-8') as file:
            text = file.read().lower()
            tokens, types, ttr = count_tokens_types_ttr(text)
            ttr_percentage = ttr * 100  # Para calcular el type-token ratio en porcentaje
            print(f'Archivo: {filename}')
            print(f'Tokens: {tokens}')
            print(f'Types: {types}')
            print(f'Type-Token Ratio (TTR): {ttr_percentage:.2f}%')
            print('----------------------------------------')
