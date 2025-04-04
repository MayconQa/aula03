import re

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))
try:
    idade = int(input("Digite a sua idade: "))
    email = input("Digite seu email: ")

    # Verifica idade
    if 18 <= idade <= 65:
          print("✅ Idade válida!")
    else:
        print("❌ Erro: Idade fora do intervalo permitido (18 a 65 anos).")
    
    # Verifica e-mail
    if validar_email(email):
        print("✅ E-mail válido!")
    else:
        print("❌ Erro: Formato de e-mail inválido.")
except ValueError:
    print("⚠️ Entrada inválida! Digite apenas números para a idade.")
