################
#Francisco Jwanczyk
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def invertir(texto):
    texto=texto.swapcase()
    return texto
def principal():
    texto=str(input("ingrese una cadena de texo con mayusculas y minusculas: "))
    print (invertir(texto))

if __name__ == "__main__":
    principal()

          