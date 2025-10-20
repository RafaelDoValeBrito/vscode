c = int(input("Digite 1 numero: "))

for c in range(1, 10):
    if c % 1 == 0 and c % c == 0:
        print(c)
    
    