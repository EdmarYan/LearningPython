#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

ganhoHora = float(input("Quanto voce ganha por horas trabalhadas no mes?\n"))
horasTrabalhadas = int(input("Quantas horas voce trabalha por dia?\n"))
ganhoMes = ganhoHora*(horasTrabalhadas*23)
print("Seu salario nesse mes foi de: ",ganhoMes)
