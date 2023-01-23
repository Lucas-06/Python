
"""
Escreva um Programa que imprime dois numeros de sua escolha
e que depois imprime a soma, a subtração, a multiplicação,
a divisão normal e a divisão inteira,
e o resto da divisão do maior pelo menor
(coloque na mensagem a palavra resto ao invez do símbolo %)

EXEMPLO DE SAÍDA:
>>> 
x = 15 
y = 10
15 + 10 = 25
15 - 10 = 5
15 x 10 = 150
15 / 10 = 1.5
15 // 10 = 1
15 resto 10 = 5
>>> 
"""
import time

x = 14
y = 7
soma = x+y
sub = x-y
multi = x*y
div = x/y
divInt = x//y
restoDiv = x%y


print("Meu número é", x)
time.sleep(1) 
print("Meu número é", y)
time.sleep(1)
print("Meu número é", soma)
time.sleep(1)
print("Meu número é", sub)
time.sleep(1)
print("Meu número é", multi)
time.sleep(1)
print("Meu número é", div)
time.sleep(1)
print("Meu número é", divInt)
time.sleep(1)
print("Meu número é", restoDiv)
time.sleep(1)
