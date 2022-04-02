import os

salario = float(input("Digite seu salário atual: "))
porcentagem = float(input("Digite a porcentagem de aumento do seu salário (ou decremento hehe): "))

x = (salario * porcentagem / 100) + salario

print ("O seu salário após o reajuste passa a ser:", x)

os.system("pause")