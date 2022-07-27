nome = input("Digite o seu nome: ")
sexo = input("Informe seu sexo: F/M ")
peso = float(input("Informe seu peso em KG: "))
altura = float(input("Informe sua altura em metros: "))
imc = peso / (altura * altura)

if sexo == 'F' :
  if imc < 19.1 :
    cond = "abaixo do peso"
  elif imc >= 19.1 and imc < 25.8 :
    cond = "no peso normal"
  elif imc >= 25.8 and imc < 27.3 :
    cond = "marginalmente acima do peso"
  elif imc >= 27.3 and imc < 32.3 :
    cond = "acima do peso ideal"
  else :
    cond = "obeso(a)"
elif sexo == 'M' :
  if imc < 20.7 :
    cond = "abaixo do peso"
  elif imc >= 20.7 and imc < 26.4 :
    cond = "no peso normal"
  elif imc >= 26.4 and imc < 27.8 :
    cond = "marginalmente acima do peso"
  elif imc >= 27.8 and imc < 31.1 :
    cond = "acima do peso ideal"
  else :
    cond = "obeso(a)"

frase = "{}, com base no peso e altura informados, o IMC é {} e a sua condição é {}".format(nome, imc, cond)
print (frase)