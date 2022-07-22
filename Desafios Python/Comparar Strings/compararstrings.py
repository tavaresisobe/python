import os

string_1 = input('Digite a primeira string: ')
string_2 = input('Digite a segunda string: ')

print ("Quantidade de caracteres de '{}': {}".format(string_1, len(string_1)))
print ("Quantidade de caracteres de '{}': {}".format(string_2, len(string_2)))
print ('As strings possuem a mesma quantidade de caracteres ?', len (string_1) == len (string_2))
print ("Os textos são iguais ?", string_1 == string_2)

os.system("pause")
