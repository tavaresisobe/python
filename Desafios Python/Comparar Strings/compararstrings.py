import os

text = input ("Digite a primeira string: ")
text2 = input ("Digite a segunda string: ")

cont = len(text)
cont2 = len(text2)

print ("Quantidade de caracteres de " + text + " é:", cont)
print ("Quantidade de caracteres de " + text2 + " é:", cont2)

check = (cont == cont2)
check2 = (text == text2)

print ("As strings possuem a mesma quantidade de caracteres:", check)
print ("As strings são iguais:", check2)
    

os.system("PAUSE")