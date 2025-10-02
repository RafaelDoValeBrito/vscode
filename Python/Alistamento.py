ano_n = int(input("Qual o seu ano de nascimento? "))
data_atual = int(input("Qualo o ano atual? "))
alistamento_idade = 18
idade_atual = data_atual - ano_n
anos_res = idade_atual - alistamento_idade

if idade_atual == 18:
    print("Momento do alistamento! ")
elif idade_atual < 18:
    print("Ainda vai se alistar no exército!\nFalta apenas {} anos para se alistar ".format(anos_res))
else:
   print("Já passou do prazo para alistamento!\nO prazo passou à {} anos! ".format(anos_res))
   

    