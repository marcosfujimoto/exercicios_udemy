#Esse programa imprime uma folha de pagamento
salhora=float(input("Informe o valor ganho por hora: "))
hour=int(input("Informa as horas trabalhadas no mês: "))
salbruto= salhora*hour
ir=0.00
if salbruto<=900:
    ir=0.00
elif salbruto<=1500:
    ir=5
elif salbruto<=2500:
    ir=10
else: 
    ir=20
descinss=salbruto*(10/100)
fgts=salbruto*(11/100)
descir=salbruto*(ir/100)
salliquido=salbruto-(descir+descinss)
print(f"Salário Bruto: (",hour,"*",salhora,")          ","R$",salbruto)
print(f"(-) IR (",ir,"%"")                                ","R$",descir)
print(f"(-) INSS (10%)                                 ","R$",descinss)
print(f"    FGTS (11%)                                 ","R$",fgts)
print(f"Total de descontos:                            ","R$",descir+descinss)
print(f"Salário Líquido:                               ","R$",salliquido)
