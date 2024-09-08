# import random
# r=random.randint(0,5)
# a=random.random()
# print(r+a)
# states=["Solid","Liquid","Gas"]
# print(states[0])
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice=random.randint(0,2)
game=[rock,paper,scissors]
print("\n \nYou chose:"+game[choice]+"\n \n \nComputer chose:"+game[comp_choice]+"\nResult:",end="")
if(choice==comp_choice):
  print("draw")
elif (choice>comp_choice and choice-comp_choice==1) or choice-comp_choice==-2:
  print("you win")
else:
  print("you loose")