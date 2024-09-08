import os

def clean():
    os.system('cls')

auction = {}
another = 'y'
t = None  # Initialize to None

while another == 'y':
    clean()
    name = input('Enter your name and bid in dollars:\n')
    bid = int(input())
    auction[name] = bid

    if t is None or bid > auction[t]:
        t = name

    clean()
    another = input("Is there another bid? Type 'y' for yes and 'n' for no. ")
    if another != 'y' and another != 'n':
        print('Invalid input')
        exit()

clean()
p = auction[t]
print(f"{t} wins the auction with a bid of ${p}")

    
