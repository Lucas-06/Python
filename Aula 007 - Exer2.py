"""
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas.
Calcule e mostre o total do seu salário no referido mês
"""

mesDia = 22

valor = int(input("Valor hora R$: "))
horas = int(input("Hora trabalhada: "))

multi = (valor*horas)

print(multi)

resultado = multi*mesDia

print(resultado)

