import random
print("GUESS THE NUMBER BETWEEN 1 AND 100!")
def guess(n):
    g=int(input("Make a guess: "))
    if g>n:
        print("Too high.")
    elif g<n:
        print("Too low.")
    else:
        print(f"You win, the number was {n}.")
        exit()
diff=input("Choose a difficulty: 'easy' or 'hard'?\n")
if diff=='easy':
    m=10
elif diff=='hard':
    m=5
else:
    print("invalid input")
    exit()
n=random.randint(1,100)
for i in range(m,0,-1):
    print(f"You have {i} attempts remaining to guess the number")
    guess(n)
print(f"You lose, the number was {n}.")




