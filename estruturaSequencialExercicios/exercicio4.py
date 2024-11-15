#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Insira sua 1º nota e tecle enter: \n"))
nota2 = float(input("Insira sua 2º nota e tecle enter: \n"))
nota3 = float(input("Insira sua 3º nota e tecle enter: \n"))
nota4 = float(input("Insira sua 4º nota e tecle enter: \n"))

calculoMedia = float(nota1+nota2+nota3+nota4)/4

print("A media final foi de ", calculoMedia)