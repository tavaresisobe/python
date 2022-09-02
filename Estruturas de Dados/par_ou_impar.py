lista = []
par = []
impar = []

while True:
  n = int(input("Informe um número (zero para sair): "))
  if n == 0:
    break
  else:
    lista.append(n)

for i in lista:
  if i % 2 == 0:
    par.append(i)
  else:
    impar.append(i)

print ("Números pares informados: ", par)
print("Números ímpares informados: ", impar)