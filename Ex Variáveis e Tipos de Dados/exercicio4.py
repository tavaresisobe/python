import os

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
maior = (a > b)
menor = (a < b)
igual = (a == b)

print("a é maior que b:",maior)
print("a é menor que b:",menor)
print("a é igual que b:",igual)

os.system("PAUSE")