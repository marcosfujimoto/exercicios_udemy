#Esse programa mostra o maior e menor número depois de uma entrada 
a= float(input("Digite um número: "))
b= float(input("Digite um segundo número: "))
c=float(input("Digite um terceiro número: "))
if a>b and a>c:
    print(f"O maior número é:", a)
elif b>a and b>c:
    print(f"O maior número é:", b)
else:
    print(f"O maior número é:", c)

if a<b and a<c:
    print(f"O menor número é:", a)
elif b<a and b<c:
    print(f"O menor número é:", b)
else:
    print(f"O menor número é:", c)
    
