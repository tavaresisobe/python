dic = {"1": ["Teclado", 300, 166.71],
       "2": ["Mouse", 125, 80.57],
       "3": ["Processador", 25, 875.64],
       "4": ["Cooler", 70, 35.14]}
j = 0
print ("Estoque:")
print ("Cód - Produto - Qtd - Valor")
for x in dic:
  print (x, "-", dic[x][0], "-", dic[x][1], "-", dic[x][2]) 
while True:
  print ("\n")
  opcao = input("Informe o código de sua ação:\n1: Registrar entrada do produto\n2: Registrar saída do produto\n3: Sair do sistema\n")
  print("\n")
  check = input(f"Você confirma a resposta anterior? S - N\n")
  if check.upper() == 'S':
    if opcao == '3':
      print("\n")
      print ("Estoque atual:")
      print ("Cód - Produto - Qtd - Valor")
      for x in dic:
        print (x, "-", dic[x][0], "-", dic[x][1], "-", dic[x][2])
      print("\n")
      print(f"O estoque teve {j} alteração(oes)")
      print("Fim do Programa.")
      break
    elif opcao == '1':
      print("\n")
      cod = input("Informe o código do produto: ")
      if cod in dic:
        qnt = int(input(f'Informe a quantidade do produto:"{dic[cod][0]}", que será incrementado no estoque: (inteiro positivo)\n'))
        dic[cod][1] += qnt
        j += 1
      else:
        print (f"Código {cod} é inválido")
    elif opcao == '2':
      print("\n")
      cod = input("Informe o código do produto: ")
      if cod in dic:
        qnt = int(input(f'Informe a quantidade do produto:"{dic[cod][0]}", que será decrementado do estoque: (inteiro positivo)\n'))
        if qnt <= dic[cod][1]:
          dic[cod][1] -= qnt
          j += 1
        else:
          print("\n")
          print("Quantidade insuficiente em estoque !!")
          print("voltando...")
      else:
        print (f"O Código {cod} é inválido")
        print("voltando...")
    else:
      print("\n")
      print("opção inválida...")
      print("voltando...")
  else:
    print("\n")
    print("voltando...")