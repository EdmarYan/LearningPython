'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
-o produto do dobro do primeiro com metade do segundo .
-a soma do triplo do primeiro com o terceiro.
-o terceiro elevado ao cubo.
'''

numero1 = int(input("Insira o primeiro numero inteiro: \n"))
numero2 = int(input("Insira o segundo numero inteiro: \n"))
numero3 = float(input("Insira o terceiro numero real: \n"))

produto = (numero1 * 2) * (numero2 / 2)
soma = (numero1 * 3) + numero3
cubo = numero3 ** 3

print("o produto do dobro do primeiro com metade do segundo :", produto
,"\na soma do triplo do primeiro com o terceiro: ", soma,
"\no terceiro elevado ao cubo:",cubo)