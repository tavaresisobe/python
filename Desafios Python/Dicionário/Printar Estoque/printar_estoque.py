dic = {"1":["Teclado", 300, 166.71],
       "2":["Mouse", 125, 80.57],
       "3":["Processador", 25, 875.64],
       "4":["Cooler", 70, 35.14],
}
print("Estoque Atual:\n")
print("Código - Produto - Qtd - Valor")
for x in dic:
  print(x, "-", dic[x][0], "-", dic[x][1], "-", dic[x][2])