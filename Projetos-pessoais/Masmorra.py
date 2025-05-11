import random

print("Seja bem-vindo a masmorra especial! ")
nome_personagem = input("Digite o nome do seu personagem: ")
print(f"Ola {nome_personagem}, qual sera sua classe? ")
def classe():
    print("Escolha uma opção: ")
    print("1 - Arqueiro")
    print("2 - Sabre")
    print("3 - Mago")
while True:
    classe()
    
    classe_escolhida = input("Digite o número da classe escolhida: ")
    if classe_escolhida == "1":
        confirmando_classe = input("A classe escolhida foi Arqueiro! Tem certeza que essa é a classe desejada? (s/n): ").lower()
        if confirmando_classe == "s":
            classe_final = "Arqueiro"
            break
        elif confirmando_classe == "n":
            continue      
    elif classe_escolhida == "2":
        confirmando_classe = input("A classe escolhida foi Sabre! Tem certeza que essa é a classe desejada? (s/n): ").lower()
        if confirmando_classe == "s":
               classe_final = "Sabre"
               break
        elif confirmando_classe == "n":
             continue       
    elif classe_escolhida == "3":
        confirmando_classe = input("A classe escolhida foi Mago! Tem certeza que essa é a classe desejada? (s/n): ").lower()
        if confirmando_classe == "s":
               classe_final = "Mago"
               break
        elif confirmando_classe == "n":
             continue
print (f"Você é {nome_personagem}, e sua classe é {classe_final}, agora voce esta pronto para explorar a masmorra especial!")

print("-" * 100)

print("Ao entrar na masmorra especial você se depara com um monstro a sua frete.")
print("Você decide atacar o monstro, os números decidiram seu destino!")
chance = random.randint(1,7)
print(f"o numero sorteado foi {chance}! ")

if chance == 1:
     print("Você errou o ataque!")
elif chance == 2:
     print("Você acertou o ataque!")
elif chance == 3:
     print("O monstro te matou!")
elif chance == 4:
     print("Você acertou o ataque!")
elif chance == 5:
     print("Você acertou o ataque!")
elif chance == 6:
     print("Você acertou o ataque!")
elif chance == 7:
     print("Você errou o ataque!")

print("-" * 100)

print("O monstro dropou um item, os números decidiram a raridade do item!")
item_chance = random.randint(1,4)
print(f"o numero sorteado foi {item_chance}! ")

if item_chance == 1:
     print("O monstro dropou um item comum!")
elif item_chance == 2:
     print("O monstro dropou um item raro!")
elif item_chance == 3:
     print("O monstro dropou um item épico!")
elif item_chance == 4:
     print("O monstro dropou um item lendario!")  

print("-" * 100)

print("Você esta ficando mais forte, porem é necessario esperar para continuar")
