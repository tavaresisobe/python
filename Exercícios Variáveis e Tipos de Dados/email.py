#Programa para obter o usuário de um endereço de email

email = input("Digite seu melhor email: ")
aux = email.index("@")
usuario = email[0 : aux]

aux_2 = email.index(".com")
provedor = email[aux+1 : aux_2]

print ("Usuário :",usuario)
print ("Provedor :",provedor)
print ("E-mail completo :",email)