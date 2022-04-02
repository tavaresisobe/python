import os

nome = input("Digite o nome do aluno: ")

nota1 = input("Digite a primeira nota do aluno: ")
nota2 = input("Digite a segunda nota do aluno: ")
nota3 = input("Digite a terceira nota do aluno: ")
nota4 = input("Digite a quarta nota do aluno: ")

media = (nota1 + nota2 + nota3 + nota4) / 4

print ("O aluno " + nome + " ficou com a média", media)

os.system("PAUSE")