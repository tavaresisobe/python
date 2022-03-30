cpf = input("Digite seu cpf com pontuação: ")
antes = cpf[0] + cpf[1] + cpf[2] + cpf[3] + cpf[4] + cpf[5]
+ cpf[6] + cpf[7] + cpf[8] + cpf[9] + cpf[10]
dhifen = cpf[12] + cpf[13]

parte1 = cpf[0]+ cpf[1] + cpf[2]
parte2 = cpf[4]+ cpf[5] + cpf[6]
parte3 = cpf[8]+ cpf[9] + cpf[10]

print ("Antes do hífen:", antes)
print ("Depois do hífen:", dhifen)
print ("Parte 1:", parte1)
print ("Parte 2:", parte2)
print ("Parte 3:", parte3)