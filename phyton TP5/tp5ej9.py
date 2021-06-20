def factorial(numero):
    factorial=1
    if numero != 0:
        for i in range (1,numero+1):
            factorial= factorial*i
    return (f"factorial:{factorial}")
def principal():
    numero=int(input("ingrese un numero:"))
    print(factorial(numero))

if __name__ == "__main__":
    principal()
          
