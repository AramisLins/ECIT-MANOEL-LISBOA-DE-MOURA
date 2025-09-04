n = int(input("Digite um número inteiro positivo: "))
numero = 2

while numero <= n:
    divisor = 2
    while divisor < numero:
        if numero % divisor == 0:
            break
        divisor += 1
    else:
        # Esse else do while só executa se não houver break
        print(numero, end=" ")
    
    numero += 1