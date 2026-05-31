import random
import os

def main(dice_choose):
    os.system('cls')
    if dice_choose == 1:
        type_dice = "d4"
        result = random.randint(1, 5)
        print(f"O valor rolado no dado {type_dice} é {result}")
    elif dice_choose == 2:
        type_dice = "d6"
        result = random.randint(1, 7)
        print(f"O valor rolado no dado {type_dice} é {result}")
    elif dice_choose == 3:
        type_dice = "d8"
        result = random.randint(1, 9)
        print(f"O valor rolado no dado {type_dice} é {result}")
    elif dice_choose == 4:
        type_dice = "d10"
        result = random.randint(1, 11)
        print(f"O valor rolado no dado {type_dice} é {result}")
    elif dice_choose == 5:
        type_dice = "d12"
        result = random.randint(1, 13)
        print(f"O valor rolado no dado {type_dice} é {result}")
    elif dice_choose == 6:
        type_dice = "d20"
        result = random.randint(1, 21)
        print(f"O valor rolado no dado {type_dice} é {result}")
    elif dice_choose == 7:
        type_dice = "d100"
        result = random.randint(1, 101)
        print(f"O valor rolado no dado {type_dice} é {result}")
    elif dice_choose == 8:
        while True:
            try:
                perso_dice = int(input("Digite qual tipo de dado que você deseja rolar: "))
                break
            except ValueError:
                print("Valor inválido! Tente novamente")
        os.system('cls')
        result = random.randint(1, perso_dice + 1)
        print(f"O valor rolado no dado de {perso_dice} lados é {result}")

os.system('cls')
print("╔══════════════════════════════════════╗")
print("║           ROLADOR DE DADOS           ║")
print("╠══════════════════════════════════════╣")
print("║                                      ║")
print("║      SELECIONE O TIPO DE DADO:       ║")
print("║                                      ║")
print("║  1. d4   (Dado de 4 faces)           ║")
print("║  2. d6   (Dado de 6 faces)           ║")
print("║  3. d8   (Dado de 8 faces)           ║")
print("║  4. d10  (Dado de 10 faces)          ║")
print("║  5. d12  (Dado de 12 faces)          ║")
print("║  6. d20  (Dado de 20 faces)          ║")
print("║  7. d100 (Dado de 100 faces)         ║")
print("║  8. Personalizado                    ║")
print("║                                      ║")
print("╚══════════════════════════════════════╝")
print("")

while True:
    try:
        dice_choose = int(input("Digite sua escolha: "))
        break
    except ValueError:
        print("Opção inválida! Tente novamente")

main(dice_choose)