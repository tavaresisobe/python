n_1 = float(input("Informe o primeiro número: "))
n_2 = float(input("Informe o primeiro número: "))
count = 0

soma = n_1 + n_2
sub = n_1 - n_2
div = n_1 / n_2
mult = n_1 * n_2

s = float(input(f"Informe o resultado da operação: {n_1} + {n_2}: "))
if (s == soma):
  print ("Você acertou !")
  count += 1
else:
  print (f"Você errou, o resultado correto é {soma}")
subtracao = float(input(f"Informe o resultado da operação: {n_1} - {n_2}: "))
if (subtracao == sub):
  print ("Você acertou !")
  count += 1
else:
  print (f"Você errou, o resultado correto é {sub:.2f}")
divisao = float(input(f"Informe o resultado da operação: {n_1} / {n_2}: "))
if (divisao == div):
  print ("Você acertou !")
  count += 1
else:
  print (f"Você errou, o resultado correto é {div:.2f}")
multiplicacao = float(input(f"Informe o resultado da operação: {n_1} * {n_2}: "))
if (multiplicacao == mult):
  print ("Você acertou !")
  count += 1
else:
  print (f"Você errou, o resultado correto é {mult:.2f}")

if count == 4:
  print("Parabéns! Você acertou todas perguntas")
elif (count > 0):
  print (f"Precisa melhorar, você acertou {count} pergunta(s)")
else:
  print ("Mandou mal! Você não acertou nenhuma pergunta")
  