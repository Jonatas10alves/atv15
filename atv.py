# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

num1 = float(input("Digite o primeiro número: "))


num2 = float(input("Digite o segundo número: "))


operacao = input("Digite a operação desejada (soma, subtração, multiplicação, divisão): ").lower()


if operacao == "soma":
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado:.2f}")
elif operacao == "subtração" or operacao == "subtracao":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado:.2f}")
elif operacao == "multiplicação" or operacao == "multiplicacao":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado:.2f}")
elif operacao == "divisão" or operacao == "divisao":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado:.2f}")
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operação inválida. Escolha entre soma, subtração, multiplicação ou divisão.")