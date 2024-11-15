'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''
ir = 0.11
inss = 0.08
sindicato = 0.05

ganhoHora = float(input("quanto voce ganha por hora?\n"))
horaDia = int(input("quantas horas voce trabalha por dia? \n"))


ganhoMes = (ganhoHora*horaDia)*23

calculoIr = ganhoMes * ir
calculoInss = ganhoMes * inss
calculoSindicato = ganhoMes * sindicato

salarioDesconto = ganhoMes - ( calculoIr + calculoInss + calculoSindicato)

print("voce pagou",calculoIr, "de IR.\n\n"
      "pagou ",calculoInss,"de INSS.\n\n",
      "e pagou ",calculoSindicato," para o sindicato.\n\n")

print("seu bruto e de: ",ganhoMes,"\n\n")
print("e o seu liquido e: ",salarioDesconto)