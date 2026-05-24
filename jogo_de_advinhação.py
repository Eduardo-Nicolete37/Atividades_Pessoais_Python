import os
import random # Importa biblioteca random para usar randint
import sys
tent = int(1) # Seta o número de tentativas para 1


# Menu de escolhas
print ("|-----------Jogo da Advinhação------------|")
print ("| Por favor, escolha a dificuldade        |")
print ("| 1: Fácil - Entre 1 e 10                 |")
print ("| 2: Médio - Entre 1 e 100                |")
print ("| 3: Difícil - Entre 1 e 1000             |")
print ("| 4: Personalizado - Você escolhe o 'teto'|")
print ("| 5: Fechar o jogo                        |")
print ()
esc = int(input(" Qual será a dificuldade desejada: ")) # esc é a variavel que encaminha para a dificuldade escolhida
os.system('cls') 

# Função principal, todo o sistema de tentativa e erro
def guess_system(number, tent):
    answer = int(input("Faça uma tentativa: "))
    while answer != number:
        if answer > number:
            print ("Incorreto! O número é MENOR, tente novamente")
            answer = int(input("Nova tentativa: "))
            tent += 1
        elif answer < number:
            print ("Incorreto! O número é MAIOR, tente novamente")
            answer = int(input("Nova tentativa: "))
            tent += 1
    else:
        print ("Parabéns! Você acertou em", tent, "tentativas")
    return tent


        

        
# Encaminhadores para dificuldade
if esc == 1:
    number = random.randint(1, 10)
    guess_system(number, tent)
elif esc == 2:
    number = random.randint(1, 100)
    guess_system(number, tent)
elif esc == 3:
    number = random.randint(1, 1000)
    guess_system(number, tent)
elif esc == 4:
    print("Por favor, digite o limite desejado: ")
    lim = int(input())
    number = random.randint(1, lim)
    guess_system(number, tent)
elif esc == 5:
  print("Jogo fechado! Volte sempre")
  sys.exit()
  
else:
  print("Opção inválida! Tente novamente")
  sys.exit()