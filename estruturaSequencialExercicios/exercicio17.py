'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
-comprar apenas latas de 18 litros;
-comprar apenas galões de 3,6 litros;
-misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
rendimentoTinta = 6
lataTinta = 18
valorLata = 80.00
galaoTinta = 3.6
valorGalao = 25.00

areaPintura = float(input("Qual será a area a ser pintada em m2? \n"))

#calculo de folga de 10%
litroNecessario = (areaPintura / rendimentoTinta) * 1.10

lataNecessaria = int(litroNecessario//lataTinta)
excedenteLata = litroNecessario % lataTinta > 0
lataNecessaria += excedenteLata
precoLata = lataNecessaria * valorLata

print(f"voce precisara de {lataNecessaria} latas e pagará {precoLata:.2f}!")

galaoNecessaria = int(litroNecessario//galaoTinta)
excedenteGalao = litroNecessario % galaoTinta > 0
galaoNecessaria += excedenteGalao
precoGalao = galaoNecessaria * valorGalao

print(f"voce precisara de {galaoNecessaria} latas e pagará {precoGalao:.2f}!")

#aqui eu tive que apelar para matematica basica, e entender como codar uma mistura:
