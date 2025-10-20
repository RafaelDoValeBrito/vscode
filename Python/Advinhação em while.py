from random import randint

computador = randint(0,10)
jogador = int(input("Chute um número de 1 a 10: "))

while jogador not in computador:
    jogador = int(input("Voçê errou, tente novamente! "))
print("Voce advinhou! O numero que eu pensei foi {}".format(jogador))
    
    