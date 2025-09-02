def soma_numeros():
    soma = 0
    while True:
        num = int(input("Digite um número (0 para sair): "))
        if num == 0:  
            break
        soma += num
    return soma



resultado = soma_numeros()
print("A soma dos números digitados foi:", resultado)