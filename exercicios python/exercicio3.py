nascimento = int(input("Informe o ano de seu nascimento: "))
idade = int(input("Informe o ano atual: "))
idade = idade - nascimento
pode_assistir = (idade >= 18)
frase = f"Você tem %d anos e a resposta é" % (idade)

print (frase, pode_assistir)
