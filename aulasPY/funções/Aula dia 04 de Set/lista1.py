#1.	Crie uma função que recebe um inteiro positivo e teste para saber se ele é primo ou não.

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  #testar até a raiz quadrada
        if n % i == 0:
            return False
    return True


num = int(input("Digite um número inteiro positivo: "))
if eh_primo(num):
    print(f"{num} é primo.")
else:
    print(f"{num} não é primo.")



#2

def imprime_triangulo(n):
    i = 1
    while i <= n:         # controla as linhas
        j = 1
        while j <= i:     # imprime de 1 até i
            print(j, end=" ")
            j += 1
        print()  # quebra de linha
        i += 1


num = int(input("Digite um número inteiro positivo: "))
imprime_triangulo(num)


#3

def maior_numero(a, b, c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior

def menor_numero(a, b, c):
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    return menor

# Programa principal
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

print(f"O maior número é: {maior_numero(n1, n2, n3)}")
print(f"O menor número é: {menor_numero(n1, n2, n3)}")
