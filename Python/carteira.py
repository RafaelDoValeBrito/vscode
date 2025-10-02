carteira = float(input("Quanto tem na carteira? "))
dolar = 3.23
comprar = carteira / dolar
print("A cotação do dolar é {}.  O dinheiro na carteira é {:.2f}.  Você pode comprar {:.2f} Reais ".format(dolar,carteira,comprar))