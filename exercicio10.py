print("Calcule o valor da multa por excedente de peso por peixe")
peso = float(input("Digite o valor do peso do peixe: "))
excedente = peso - 50
multa = excedente*4.0
print(f"O valor de peso excedente foi: ", excedente, "em razão disso, a multa a ser paga será de ","R$", multa)
