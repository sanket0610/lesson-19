import random
opt=["rock","paper","scissor"]
us=input("CHOOSE ROCK,PAPER OR SCISSOR: ")
cs=random.choice(opt)
print("COMPUTER SELECTED:",cs)
print("USER SELECTED:",us)
if us==cs:
    print("ITS A TIE!")
elif us=="rock" and cs=="scissor":
    print("YOU WIN!")
elif us=="paper" and cs=="rock":
    print("YOU WIN!")
elif us=="scissor" and cs=="paper":
    print("YOU WIN!")
else:
    print("COMPUTER WINS")