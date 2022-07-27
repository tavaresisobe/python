nome = input("Informe o nome do aluno: ")
nota_1 = float(input("Informe a primeira nota: "))
nota_2 = float(input("Informe a segunda nota: "))
nota_3 = float(input("Informe a terceira nota: "))
nota_4 = float(input("Informe a quarta nota: "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media < 5.0 :
  resultado = "reprovado"
elif media >= 5.0 and media < 7.0 :
   resultado = "de recuperação"
elif media >= 7.0 :
  resultado = "aprovado"

print ("O aluno {} está {}. Sua média foi {}".format(nome, resultado, media))