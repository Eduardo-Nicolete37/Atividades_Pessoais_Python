from texasholdem import Card
from texasholdem.evaluator import evaluate, rank_to_string
import os

def avaliar_pre_flop(hole_cards, cartas_user):
    card1 = max(hole_cards[0].rank, hole_cards[1].rank)
    card2 = min(hole_cards[0].rank, hole_cards[1].rank)
    suited = hole_cards[0].suit == hole_cards[1].suit
    pair = card1 == card2

    score = card1 + card2
    if pair:
        score += 10
    if suited:
        score += 3
    if card1 - card2 <= 1:
        score += 2
    if card1 - card2 <= 2:
        score += 1
    if card1 - card2 > 4:
        score -= 1
    if card1 < 5:
        score -=3
    if pair:
        percentual = round((score/39) * 100)
    if not pair:
        percentual = round((score/28) * 100)



    if (pair and card1 >= 10) or (card1 == 12 and card2 == 11) or (card1 == 12 and card2 == 10):
        os.system('cls')
        print(f"{' '.join(cartas_user)} é uma mão extremamente boa!")
        print("Recomendo RAISE alto, mas tenha cuidado.")
        print("Para evitar que os jogadores 'foldem', não seja extremamente agressivo")
        print(f"Equidade estimada: {percentual}%")
    elif (pair and card1 <= 9 and card1 >= 5) or (not suited and card1 == 12 and card2 == 10):
        os.system('cls')
        print(f"{' '.join(cartas_user)} é uma mão forte!")
        print("Recomendo RAISE não agressivo, mas tenha cuidado.")
        print("Sua mão pode ser neutralizada de forma relativamente fácil.")
        print(f"Equidade estimada: {percentual}%")
    elif (not suited and card1 == 12 and card2 == 9) or (suited and card1 == 11 and card2 == 10):
        os.system('cls')
        print(f"{' '.join(cartas_user)} é uma mão forte!")
        print("Recomendo RAISE não agressivo, mas tenha cuidado.")
        print("Sua mão pode ser neutralizada de forma relativamente fácil.")
        print(f"Equidade estimada: {percentual}%")
    elif (pair and card1 >=0 and card1 <= 4) or (suited and card1 + card2 >= 19) or (suited and card1 >=4 and card1 <= 7 and card1 - card2 <= 2):
        os.system('cls')
        print(f"{' '.join(cartas_user)} é uma mão forte!")
        print("Recomendo apenas fazer o CALL.")
        print("É uma mão forte, mas não o suficiente para RAISE")
        print(f"Equidade estimada: {percentual}%")
    elif (not suited and card1 + card2 >= 19 and card1 !=12) or (suited and card1 - card2 <= 2 and card1 >= 1 and card1 <= 3):
        os.system('cls')
        print(f"{' '.join(cartas_user)} é uma mão relativamente forte!")
        print("Recomendo apenas fazer o CALL caso esteja em um posição boa.")
        print("Ex: Button, Cutoff ou Hijack (ou seja, posições tardias)")
        print("É uma mão boa, mas não o suficiente para CALL de qualquer forma")
        print(f"Equidade estimada: {percentual}%")
    else:
        os.system('cls')
        print(f"{' '.join(cartas_user)} é NÃO é uma mão boa!")
        print("Recomendo fazer o FOLD")
        print("É uma mão péssima")
        print(f"Equidade estimada: {percentual}%")

    
os.system('cls')
print("╔══════════════════════════════════════╗")
print("║   🃏  TEXAS HOLD'EM ADVISOR  🃏      ║")
print("╠══════════════════════════════════════╣")
print("║                                      ║")
print("║   Como escrever suas cartas:         ║")
print("║   Ranks:  2 3 4 5 6 7 8 9 T J Q K A  ║")
print("║   Naipes: h=♥  d=♦  c=♣  s=♠         ║")
print("║                                      ║")
print("║   Exemplos:  As = Ás de espadas      ║")
print("║              Kh = Rei de copas       ║")
print("║              Td = 10 de ouros        ║")
print("║                                      ║")
print("║      Escreva as cartas SEPARADAS     ║")
print("║   Exemplo: As Kh                     ║")
print("║                                      ║")
print("╚══════════════════════════════════════╝")

cartas_user = input("Digite as suas cartas na notação descrita acima: ").split()
hole_cards = [Card(c) for c in cartas_user]

os.system('cls')
fases = {"1": "PRE-FLOP", "2": "FLOP", "3": "TURN", "4": "RIVER"}
print("Qual é a fase atual?")
for k, v in fases.items():
    print(f"  {k}. {v}")
fase_key = input("Fase (1-4): ").strip()
fase = fases.get(fase_key, "FLOP")

if fase_key == "1":
    avaliar_pre_flop(hole_cards, cartas_user)