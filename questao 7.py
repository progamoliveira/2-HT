num1 = int(input("Informe o primeiro número: "))


num2 = int(input("Informe o segundo número: "))


num3 = int(input("Informe o terceiro número: "))


if num1 <= num2 and num1 <= num3:
    menor = num1


elif num2 <= num1 and num2 <= num3:
    menor = num2


else:
    menor = num3
print("O menor número é o número:", menor)
