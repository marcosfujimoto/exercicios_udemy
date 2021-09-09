#programa para cálculo de ajuste de salário
salanterior=float(input("Informe o seu salário: "))
salatual=0.0
percentualdeaumento=0.0
difsalario=0.0

if salanterior<=280.00:
    percentualdeaumento=20
elif salanterior<=750:
    percentualdeaumento=15
elif salanterior<=1500:
    percentualdeaumento=10
else:
    percentualdeaumento=5

difsalario= salanterior*(percentualdeaumento/100)
salatual=salanterior+difsalario
print(f"Seu salário anterior era: R$", salanterior)
print(f"O seu salário teve um aumento de:", percentualdeaumento,"%")
print(f"O aumento foi de: R$", difsalario)
print(f"Esse é o seu novo salário: R$", salatual)


