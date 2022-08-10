num = int(input("Informe o número que você quer treinar a tabuada: "))
i = 1
acertos = 0
erros = 0
print ("Responda:")
while (i <= 10):
  aux = num * i
  tent = int(input(f"{num} x {i}: "))
  if (tent == aux):
    print ("Correto !")
    acertos += 1
  else:
    print (f"Que pena, você errou, o valor correto é {aux}")
    erros += 1
  i += 1
print (f"Total de acertos {acertos}")
print (f"Total de erros {erros}")