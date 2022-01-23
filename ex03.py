nascimentoDia = int(input("Digite a data de nascimento: "))
nascimentoMes = int(input("Digite o mês que nasceu: "))

if nascimentoDia <=10: 
    print("Tipo Pedra")

elif nascimentoDia >=22:
    print("Tipo fantasma")

else:
    print("Tipo Elétrico")

if nascimentoMes <=3:
    print("Fogo")

elif nascimentoMes >=8:
    print("Planta")

else:
    print("Água")

    

    