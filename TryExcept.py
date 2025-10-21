# 1 Questão
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado:.2f}")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")

# 2 Questão
try:
    numero = float(input("Digite um número: "))
    print(f"Você digitou o número {numero}")

except ValueError:
    print("Erro: Você deve digitar apenas números!")

# 3 Questão
try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a / b
    print(f"Resultado da divisão: {resultado:.2f}")

except ValueError:
    print("Erro: Você digitou um valor inválido. Use apenas números!")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")

# 4 Questão
def dividir(a, b):
    try:
        resultado = a / b
        return f"Resultado: {resultado:.2f}"
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."
    except TypeError:
        return "Erro: Os valores devem ser numéricos."

try:
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    print(dividir(x, y))
except ValueError:
    print("Erro: Digite apenas números válidos!")