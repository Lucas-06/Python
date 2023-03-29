"""
O jovem tem idade, só pode entrar maior de 18 anos ?
"""

idade = int(input("Digite sua idade: "))

if(idade >= 18):
    print("Voce passou, sua idade é:", idade)
    if(idade >= 21):
        print("Voce é VIP")
    
else:
    print("Voce é muito jovem NÃO pode entrar")





