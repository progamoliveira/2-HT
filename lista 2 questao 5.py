P = float(input("Informe o peso de peixes em quilos: "))

if P > 50:
    
    E = P - 50
    M = E * 4
else:
    
    E = 0
    M = 0

# Imprime o resultado
print("Excesso de peso: ", E, "kg")
print("Valor da multa: R$", M)
