temperatura = int(input("Digite o valor da temperatura ideal: "))

if temperatura < 18:
    print(f"Temperatura {temperatura} considerada baixa!")
elif 18 <= temperatura <= 26:
    print(f"Temperatura {temperatura} considerada Média!")
else:
    print(f"Temperatura {temperatura} considerada Alta!")