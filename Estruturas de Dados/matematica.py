lista = []
soma = 0
multiplicacao = 1
while True:
  num = int(input("Digite o número / Informe 0 (zero) para parar: "))
  if num == 0:
    break
  else:
    lista.append(num)

for i in lista:
  soma += i
  multiplicacao *= i

print (f"Soma: {soma}")
print (f"Multiplicação: {multiplicacao}")
print(f"O maior: {max(lista)}")
print(f"O menor: {min(lista)}")