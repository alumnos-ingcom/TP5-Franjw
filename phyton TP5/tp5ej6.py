
def cadena_de_parentesis(cadena):
    fila=[]
    parentesis={' {' :' }' ,' (' :' )' ,' [' :' ]' }
    
    for i in cadena:
        if i in parentesis:
            fila.append(i)
        elif len(fila)==0 or i != parentesis[fila.pop()]:
            return ("no es una cadena")
    return len(fila)==0

        
def principal():
    cadena=input("ingrese una serie de parentesis")
    print(cadena_de_parentesis(cadena))

if __name__ == "__main__":
    principal()