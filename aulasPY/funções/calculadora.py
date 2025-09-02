def soma(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mult(a,b):
    return a*b
    
def div(a,b):
    return a/b
    
while True:
    print("Bem vindo a calculadora !!!")
    print("1 - soma")
    print("2 - sub")
    print("3 - mult")
    print("4 - div")
    print("0 - sair")
    n = int(input("--->"))
    if n ==1:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print(soma(n1,n2))
    elif n ==2:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print(sub(n1,n2))    
    elif n ==3:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print(mult(n1,n2))
    elif n ==4:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print(div(n1,n2))
    elif n == 0:
        print("finish")
        break