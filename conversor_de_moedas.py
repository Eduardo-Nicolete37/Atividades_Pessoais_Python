import os
import sys
import requests
os.system('cls')
puller = ""


print("╔═════════════════════════════════════════╗")
print("║           Conversor de Moedas           ║")
print("╠═════════════════════════════════════════╣")
print("║                                         ║")
print("║ De qual moeda você deseja converter?    ║")
print("║ 1 - Real(R$)                            ║")
print("║ 2 - Dolár($)                            ║")
print("║ 3 - Euro(€)                             ║")
print("║ 4 - Libra(£)                            ║")
print("║                                         ║")
print("╚═════════════════════════════════════════╝")
print()
while True:
    try:
        in_money = int(input("Escolha: "))
        break
    except ValueError:
        os.system('cls')
        print("Opção inválida, tente novamente")

os.system('cls')
if  in_money == 1:
    puller = "BRL-"
    first = "Real"
    starter = "R$"
elif in_money == 2:
    puller = "USD-"
    first = "Dolár"
    starter = "$"
elif in_money == 3:
    puller = "EUR-"
    first = "Euro"
    starter = "€"
elif in_money == 4:
    puller = "GBP-"
    first = "Libra"
    starter = "£"
else:
    print("MOEDA FORA DA LISTA! TENTE NOVAMENTE")
    sys.exit()
    

print("╔═════════════════════════════════════════╗")
print("║           Conversor de Moedas           ║")
print("╠═════════════════════════════════════════╣")
print("║                                         ║")
print("║ Para qual moeda você deseja converter?  ║")
print("║ 1 - Real(R$)                            ║")
print("║ 2 - Dolár($)                            ║")
print("║ 3 - Euro(€)                             ║")
print("║ 4 - Libra(£)                            ║")
print("║                                         ║")
print("╚═════════════════════════════════════════╝")
print()
while True:
    try:
        out_money = int(input("Escolha: "))
        break
    except ValueError:
        os.system('cls')
        print("Opção inválida, tente novamente")

os.system('cls')
if  out_money == 1:
    puller += "BRL"
    last = "Real"
    final = "R$"
elif out_money == 2:
    puller += "USD"
    last = "Dolár"
    final = "$"
elif out_money == 3:
    puller += "EUR"
    last = "Euro"
    final = "€"
elif out_money == 4:
    puller += "GBP"
    last = "Libra"
    final = "£"
else:
    print("MOEDA FORA DA LISTA! TENTE NOVAMENTE")
    sys.exit()

os.system('cls')

if in_money == out_money:
    print("MOEDAS IGUAIS! TENTE NOVAMENTE ESCOLHENDO OUTRAS OPÇÕES")
    sys.exit()
    


count = float(input("Digite o quanto você quer converter: "))

request = requests.get(f'https://economia.awesomeapi.com.br/json/last/{puller}')
dados = request.json()

chave = puller.replace("-", "")
valor_moeda = float(dados[chave]["bid"])
valor_moeda_final = count * valor_moeda
os.system('cls')

print(f"A conversão do(a) {first} para o(a) {last} é: {final}{valor_moeda:.2f}")
print(f"Multiplicado por {starter}{count}, é igual á: {final} {valor_moeda_final:.2f}")