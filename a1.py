import random
play=True
n=random.randint(10,20)
print("GUESS THE NUMBER BETWEEN 10 AND 20. THIS GAME WILL END IF YOU GUESS THE CORRECT NUMBER")
while play:
    g=int(input("ENTER YOUR GUESS"))
    if g==n:
        print("YOU WIN!THE CORRECT NUMBER WAS", n)
        break
    else:
        print("TRY AGAIN")