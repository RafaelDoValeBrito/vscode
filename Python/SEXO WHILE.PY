sexo = str(input("Qual é o seu sexo? "))
while sexo not in 'mMfF':
    sexo = str(input("Digite novamente! "))
print(" O seu sexo é {} ".format(sexo))
    
