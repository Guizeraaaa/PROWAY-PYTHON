nota01 = int(input("Digite a nota 1: "))
nota02 = int(input("Digite a nota 2: "))
nota03 = int(input("Digite a nota 3: "))
media = (nota01+nota02+nota03) /3
# nome = input("Digite seu nome")
# sobrenome = input("Informe seu sobrenome")
# idade = input("Informe a sua idade")

if media <= 5: 
    print("Você reprovou")
   
elif media >=7:
    print("Parabéns você passou")

else:   
    print("Você está em recuperação")



# print(nome + sobrenome + idade) 
print("A sua média foi de : ",media)

