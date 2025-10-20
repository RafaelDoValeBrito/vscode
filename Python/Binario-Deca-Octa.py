
print('''Escolha uma das bases para conversão:
[1] Converter para binario
[2] Converter para Decadeximal
[3] Converter para Octa ''')

num = int(input("Digite um número: "))

if num == 1:
  print("{} Convertido para binário é igual {}").format(num, bin(num)[2:])
elif num == 2:
      print("{} Convertido para Hexadecimal é igual {}").format(num, hex(num)[2:])
elif num == 3:
      print("{} Convertido para Octadecimal é igual {}").format(num, oct(num)[2:])
else:
      print("Resultado inválido! ")
      
