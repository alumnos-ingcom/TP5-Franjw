################
# Francisco Jwanczyk
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def numeropar(numero):
    division=float(numero) /2
    if str(division).endswith("0") == True:
        return True
    else:
        return False

def principal():
    numero=int(input("ingrese un numero: "))
    print(numeropar(numero))

if __name__ == "__main__":
    principal()