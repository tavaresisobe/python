list = []

while True:
  palavra = input("Informe uma palavra / Digite 0 (zero) para SAIR: ")
  if palavra == '0':
    break
  else:
    list.append(palavra)
set = set(list)
print (f"Lista de palavras sem repetição:")

for i in set:
  print (i)

