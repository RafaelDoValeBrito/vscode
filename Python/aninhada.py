casa = float(input("QUal o valor da casa que irá comprar? "))
salario = float(input("QUal o seu salario? "))
anos = int(input("Em Quantos anos vai pagar? "))
mensalidade = anos * 12
prestacao = casa / mensalidade
pretencao = salario * 0.30

print("O valor da prestação será de {:.2f} ".format(prestacao))
if prestacao > pretencao: 
    print("Emprestimo negado! ")
else:
    print("Emprestimo aceito! ")
    
