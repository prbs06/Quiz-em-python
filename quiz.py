print("Seja muito bem vindo no quiz do Paulo")
answer_user = input("Quer começar (S/N) ")

if answer_user !="S":
    quit()
    
    score = 0
    
print("Começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n ")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correct")
    score = score + 1
else:
    print("Incorreto!")
    
print("Qual o nome do protagonista do jogo GTA San Andreas? \n (A) Carlos John \n (B) Carl jaqueline \n (C) Carlos Jonson \n (D) EA \n ")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Correto")
    score = score + 1
else:
    print("Incorreto!")
    print("Quiz acabou... \n Pontuação: {score}/2")