print("Esse programa informará se você foi aprovado ou não em uma disciplina")
a= float(input("Insira a primeira nota: "))
b= float(input("Insira a segunda nota:  "))
print("Calculando notas")
media= (a+b) /2
if media >7:
    print(media , "Aprovado")
else:
    print(media , "Reprovado")

