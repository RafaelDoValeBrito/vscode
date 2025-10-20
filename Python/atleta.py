ano_n = int(input("O ano de nascimento: "))
dias_atuais = 2025 - ano_n 

if dias_atuais <= 9:
    print("Mirim")
elif dias_atuais < 15:
    print("Infatil")
elif dias_atuais <19:
    print("Junior")
elif dias_atuais <20:
    print("Sênior")
else:
    print("Master")