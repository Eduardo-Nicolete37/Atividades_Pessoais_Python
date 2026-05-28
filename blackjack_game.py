# Bibliotecas que vou usar
import os # Para os.system
import random # Embaralar as cartas
import time # Pausa entre entrega de cartas
import sys # Para o código caso o jogador faça merda ou perca

baralho = ["2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh", "Ah", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc", "Ac", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd", "Ad", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks", "As"]
valor_face_cards = {
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}
random.shuffle(baralho) # Embaralhamento das cartas

def jogo_central(baralho):
    print # print como placeholder por agora

