################
#Francisco Jwanczyk
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def palabras(palabra,texto):
    posicion=texto.find(palabra)
    return (f"la palabra esta en la posicion {posicion}, contada desde el inicio")

def principal():
    texto=input("escriba un texto:")
    palabra=input("ingrese la palabra que busca:")
    print(palabras(palabra,texto))

if __name__ == "__main__":
    principal()



    