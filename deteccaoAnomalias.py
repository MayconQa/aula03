transacao = {'valor': 10000, 'hora': 18}

# Validação do valor
if transacao["valor"] > 10000:
    print(f"transação {transacao["valor"]} é considerada suspeita")
else:
    print(f"Transação {transacao["valor"]} dentro do valor permitido")

# Validação da hora se ocorrer fora do horário comercial (antes das 9h ou depois das 18h)
if 9 < transacao["hora"] and transacao["hora"] > 18:
    print(f"transação {transacao["hora"]} é considerada suspeita")
else:
    print(f"Transação {transacao["hora"]} dentro do horario comercial permitido")