quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço: "))
if quantidade <= -1:
    print(f"Quantidade {quantidade} é inválido")
else:
    print("Quantidade é válido")
 
if preco <= -1:
    print(f"Preço {preco} é inválido")
else:
    print("Preço válido")