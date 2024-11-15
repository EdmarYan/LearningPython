# Data for the employees (name, age, salary)
data = [
    "edmar 22 2400",
    "leticia 20 4000",
    "daniel 27 3500",
    "flavia 29 6000"
]

maiorSalario = 0
total = 0

# Loop through each employee entry
for i in range(4):
    item = data[i].split(" ")
    nome = str(item[0])
    idade = int(item[1])
    salario = float(item[2])

    total += salario
    
    # Check if the current salary is higher than the previously stored one
    if salario > maiorSalario:
        maiorSalario = salario

# Output the results
print(f"Maior salário: {maiorSalario}")
print(f"Soma total dos salários: {total}")
