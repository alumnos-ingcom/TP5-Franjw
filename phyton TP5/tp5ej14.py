def capicua(numero):
    if numero < 0:
        return ("el numero debe ser positivo")
    elif numero >=0:
        if str(numero)==str(numero)[::-1]:
            return("es capicua")
        else:
            return ("no es capicua")
            

def principal():
    numero=int(input("ingrese un numero positivo"))
    print(capicua(numero))
    
if __name__ == "__main__":
    principal()
          
               
