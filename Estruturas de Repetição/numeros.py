qnt = int(input("Informe a quantidade de números que de 1-9: "))
soma = 0
count = 1
string = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'sétimo', 'oitavo', 'nono']
if qnt < 1 or qnt > 9:
  print ("Quantidade de números é inválida")
else:
  while qnt > 0:
    n = int(input(f"Informe o {string[count - 1]} número: ")) #leitura dos números
    soma += int(n * count)  #variavel para armazenar a soma e multiplicação dos números
    qnt -= 1  #variáveis auxiliares:
    count += 1
print (f"O reseultado final é: {soma}")