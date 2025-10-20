import time

numero = int(input("Digite um numero: "))

print("Numero da tabuada escolhido: {}".format(numero))
time.sleep(1)

for i in range (1, 11):
    resultado = numero * i
    print("A multiplicação de {} x {} é igual a: {} ".format(numero, i, resultado ))
    