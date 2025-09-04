def fatorial(n):
    resultado = 1
    contador = n
    
    while contador > 1:
        resultado *= contador
        contador -= 1
    
    return resultado

numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("Não existe fatorial de número negativo!") #verificando se o numero que o usuário digitou é negativo
else:
    print(f"O fatorial de {numero} é {fatorial(numero)}") #chamando a função fatorial


