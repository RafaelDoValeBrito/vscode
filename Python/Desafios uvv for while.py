'''num = int(input("Digite um número! "))

somap = 0
somai = 0

while num != 999:
    if num  % 2 == 0:
        somap += num
    else:
        somai += num
        
    print("Tente Novamente ")
    num = int(input("Digite um número: "))
    
print("Acertou")

diferenca = somap - somai

print("--- Resultado ---")
print("A diferença entre os dois é de {}".format(diferenca))
print("A soma dos nuemros pares é {}".format(somap))
print("A soma dos nuemros impares é {}".format(somai))'''

nomes = []

for i in range(0,5):
    nome = str(input("Digite seu nome "))
    nomes = nomes + [nome]
    
print(nomes)


























