'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

tamanhoPintura = float(input("Qual será o tamanho da área em metros quadrados que será pintada? "))


coberturaPorLitro = 3  # Cobertura de 1 litro para 3 m²
capacidadeLata = 18  # 18 litros por lata
precoLata = 80.00  # Preço por lata

litrosNecessarios = tamanhoPintura / coberturaPorLitro
latasNecessarias = int(litrosNecessarios // capacidadeLata)  # Número inteiro de latas, e '//' retorna apenas o inteiro
excedente = (litrosNecessarios % capacidadeLata > 0)  # Se houver excesso, será 1 (True), senão 0 (False)
# O operador % é o operador de módulo. Ele retorna o resto da divisão entre dois números. Por exemplo, 
# 7 % 3 resulta em 1, porque 7 dividido por 3 é igual a 2 com resto 1.

# Se houver excesso, somar mais uma lata
latasNecessarias += excedente
precoTotal = latasNecessarias * precoLata

# Output

print(litrosNecessarios)
print(latasNecessarias)
print(f"Você precisará de {latasNecessarias} latas de tinta.")
print(f"O custo total será de R$ {precoTotal:.2f}.")
