################
#Francisco Jwanczyk
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def binario1(numero):
    binario=bin(numero)
    return (format(numero,"0b"))


def numerob(binario):
    numerobinario=int(binario, base=2)
    return numerobinario

def principal():
    intobin=int(input("ingrese 1 para entero a binario o 2 para binario a entero: "))
    if intobin == 1:
        numero=int(input("ingrese un numero entero para transformar a binario: "))
        print(binario1(numero))
    elif intobin ==2:
        binario=input("ingrese un numero binario: ")
        print(numerob(binario))
    else:
        print("no es una opcion")
    

if __name__ == "__main__":
    principal()