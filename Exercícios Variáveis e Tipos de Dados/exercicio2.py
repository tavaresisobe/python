import os

v_compra = float(input("Informe o valor da compra: "))
parcelas = int(input("Informe o número de parcelas: "))
v_parcelas = v_compra / parcelas
frase = f"O valor da compra foi de %f, o número de parcelas informado foi %d e o valor da parcela é %.3f" % (v_compra, parcelas, v_parcelas)

print (frase)

os.system("pause")
