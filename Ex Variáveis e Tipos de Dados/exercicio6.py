import os

cpf = input("Digite seu cpf com pontuação: ")
dhifen = cpf[12:14]
antes = cpf[0:11]

parte1 = cpf[0:3]
parte2 = cpf[4:7]
parte3 = cpf[8:11]

print ("Antes do hífen:", antes)
print ("Depois do hífen:", dhifen)
print ("Parte 1:", parte1)
print ("Parte 2:", parte2)
print ("Parte 3:", parte3)

os.system("pause")