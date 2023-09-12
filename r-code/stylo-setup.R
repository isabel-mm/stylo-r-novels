  # INSTALACIÓN Y ACTIVACIÓN DE LA LIBRERÍA
install.packages("stylo")

library(stylo)

  # ENCONTRAR DIRECTORIO DE TRABAJO ACTUAL
getwd()

  # CAMBIAR DIRECTORIO DE TRABAJO
setwd("tu/directorio")


# stylo() | Mide la distancia entre dos sets de textos

  # Preparación del corpus:

    # El corpus debe estar en una carpeta llamada 'corpus' alojada en tu directorio de trabajo
    # Los archivos deben estar codificados siguiendo el esquema Autor_Título.txt (o .html/.xml)
    # Para saber qué archivos se encuentran en el directorio:

list.files()
  
    # Para ejecutar stylo()
  
stylo()


# oppose() | Compara dos sets de textos y produce un diagrama de las preferencias léxicas de cada grupo/subcorpus

    # En el directorio tiene que haber dos carpetas de textos: 'primary_set' y 'secondary_set'

    # Para ejecutar oppose()

oppose()
