casa = float(input("Qual o valor da casa que irá comprar? "))
salario = float(input("Qual o seu salario? "))
anos = int(input("Em Quantos anos vai pagar? "))
prestacao = casa / (anos * 12)
minimo = salario * 30/100

print("O valor da prestação será de {:.2f} ".format(prestacao))
if prestacao <= minimo: 
    print("Emprestimo negado! ")
else:
    print("Emprestimo aceito! ")
    
