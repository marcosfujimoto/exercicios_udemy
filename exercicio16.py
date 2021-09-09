#Esse programa lê qual número é maior entre uma entrada de números
n1= float(input("Digite um número: "))
n2= float(input("Digite um número: "))
n3= float(input("Digite um número: "))
if n1> n2 and n1 > n3 :
    print("O número maior é", n1)
elif n2> n1 and n2> n3:
    print("O número maior é", n2)
else: 
    print("O número maior é", n3)
