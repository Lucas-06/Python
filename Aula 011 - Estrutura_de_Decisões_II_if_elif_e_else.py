"""
Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
	Observando os termos no plural a colocação do "e", da vírgula
	entre outros. Exemplo:
	326 = 3 centenas, 2 dezenas e 6 unidades
	12 = 1 dezena e 2 unidades
	Testar com: 326, 300, 100, 320, 310,305, 301,
	101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

valor = int(input("Digite o valor: "))
valor_resultado = valor

if  valor > 0 and valor <= 1000:
    centena = valor // 100
    valor = valor % 100
    
    dezena = valor // 10
    valor = valor % 10
    
    unidade = valor // 1
    valor = valor % 1
                               
 
    if centena == 1 and dezena != 1 and unidade != 1:
        print(valor_resultado, " = ", centena, "Centena,", dezena, "Dezenas e ", unidade, "Unidades")
       
    elif dezena == 1 and centena != 1 and unidade != 1:
        print(valor_resultado, " = ", centena, "Centenas,", dezena, "Dezena e ", unidade, "Unidades")
        
    elif unidade == 1 and dezena != 1 and centena != 1:
        print(valor_resultado, " = ", centena, "Centenas,", dezena, "Dezenas e ", unidade, "Unidade")

    elif centena > 1  and dezena > 1 and unidade > 1:
        print(valor_resultado, " = ", centena, "Centenas,", dezena, "Dezenas e ", unidade, "Unidades")

    elif centena > 1 and dezena == 0 and unidade == 0:
        print(valor_resultado, " = ", centena, "Centenas,", dezena, "Dezenas e ", unidade, "Unidades")

    elif centena >1 and dezena > 1 and unidade == 0:
        print(valor_resultado, " = ", centena, "Centenas,", dezena, "Dezenas e ", unidade, "Unidades")

    elif centena > 1 and dezena == 0 and unidade > 1:
        print(valor_resultado, " = ", centena, "Centenas,", dezena, "Dezenas e ", unidade, "Unidades")

    elif centena == 1 and dezena == 0 and unidade == 1:
        print(valor_resultado, " = ", centena, "Centena,", dezena, "Dezenas e ", unidade, "Unidade")

    elif centena > 1 and dezena == 1 and unidade == 1:
        print(valor_resultado, " = ", centena, "Centenas,", dezena, "Dezena e ", unidade, "Unidade")

    elif centena == 1 and dezena == 1 and unidade == 1:
        print(valor_resultado, " = ", centena, "Centena,", dezena, "Dezena e ", unidade, "Unidade")

    elif centena == 0 and dezena > 1 and unidade > 1:
        print(valor_resultado, " = ", dezena, "Dezenas e ", unidade, "Unidades")

    elif centena == 0 and dezena == 1 and unidade == 1:
        print(valor_resultado, " = ", dezena, "Dezena e ", unidade, "Unidade")

    elif centena == 0 and dezena > 1 and unidade == 0:
        print(valor_resultado, " = ", dezena, "Dezenas e ", unidade, "Unidades")

    elif centena == 0 and dezena == 0 and unidade > 1:
        print(valor_resultado, " = ", dezena, "Dezenas e ", unidade, "Unidades")


else:
    print("Não é possivel realizar a operação")

"""
  print(f'{valor_resultado} = {centena} Centena, {dezena} ,{unidade}')
 """








