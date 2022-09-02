lista = []
aux = 0
while True:
  palavra = input("Informe uma palavra (zero para sair): ")
  if palavra == '0' or palavra == 'zero':
    break
  else:
    lista.append(palavra.upper())
check = input("Informe a palavra que deseja contar: ")

for i in lista:
  if i == check.upper():
    aux += 1
    
print(f"Temos {aux} ocorrências de {check}")