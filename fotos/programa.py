print("Olá, fui programado para lhe ajudar a saber o valor aproximado da sua conta de energia,")
print("mas para isso vou precisar de algumas informações.")
print()

consumo = int(input("Qual é o consumo em kWh: "))
tipo = input('''Qual é o tipo da instalação?

[1] Residencial
[2] Comérial
''')


if tipo == '1':
    if consumo == consumo:
        preço = 0.735840
elif tipo == "2":
    if consumo == consumo:
        preço = 0.736610
else:
    preço = 0
    print("Erro! Tipo de instalação desconhecido!")
    
print()
custo = (consumo * preço)

print('-' * 30)
print(f"Valor a pagar: R$ {custo:7.2f}")
print('-' * 30)
print("OBS:Esse programa não considera nenhuma das bandeira e nenhum tipo de multa.")


