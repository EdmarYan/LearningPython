#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

fahrenheit = float(input("insira a temperatura em Fahrenheit e tecle enter: \n"))

conversao = 5 * ((fahrenheit-32) / 9)

print("A conversão da temperatua e de: ", conversao)