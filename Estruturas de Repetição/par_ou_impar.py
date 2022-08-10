ler = input("Informe um número ou 'sair' para finalizar: ")
frase = "é um número"
while (ler != 'sair'):
  i = int(ler)
  if (i % 2 == 0 ):
    print(f"{i} {frase} par.")
  else:
    print (f"{i} {frase} ímpar.")
  ler = input("Informe um número ou 'sair' para finalizar: ")
print ("Sistema finalizado.")