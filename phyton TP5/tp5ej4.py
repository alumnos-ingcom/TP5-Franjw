################
# Francisco Jwanczyk
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def numero_perfecto(numero):
    suma= 0
     
    for i in range (1,numero):
        
        if numero % i==0:
            suma +=i
    return suma ==numero
      
def principal():
    numero=int(input("ingrese un numero para saber si es perfecto"))
    print(numero_perfecto(numero))

if __name__ == "__main__":
    principal()