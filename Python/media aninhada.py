nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1 + nota2)/ 3
if media < 5:
    print("Reprovado")
elif media >= 5 or media <6.9:
    print("Recuperação")
else:
    print("Passou")