import os

valor = float(input("Digite o valor das parcelas do produto: "))
parcelas = int(input("Digite o numeros de parcelas: "))

total = valor * parcelas 
frase = "O valor da compra é: %.2f" % total

print (frase)

os.system("PAUSE")