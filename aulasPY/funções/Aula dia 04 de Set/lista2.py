def soma_dois_numeros(num1, num2):
    return num1 + num2

# Exemplo de uso
print("Soma:", soma_dois_numeros(10, 5))


# 2. Função para Calcular IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")

# Exemplo de uso
calcular_imc(70, 1.75)


# 3. Função para Dobro de um Número
def dobro(numero):
    return numero * 2

# Exemplo de uso
print("Dobro:", dobro(7))


# 4. Função de Conversão de Temperatura (Celsius para Fahrenheit)
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Exemplo de uso
print("Temperatura em Fahrenheit:", celsius_para_fahrenheit(30))