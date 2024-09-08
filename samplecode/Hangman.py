# import random
# word_list = ["aardvark", "baboon", "camel"]
# word = word_list[random.randint(0, 2)]
# p = word
# p = p.lower()
# p=list(p)
# r=['_']*len(word)
# c,q = 0,0
# o=p
# while o != '':
#     guess = input("Guess a letter\n")
#     for i in range(len(p)):
#         if p[i] == guess:
#             o.remove(o[i])
#             c += 1
#             r[i]=p[i]
#     if c >= 1:
#         print(f"The letter is present {c} times")
#     else:
#         print("The letter is not present")
#     if c == 0:
#         q += 1
#     print(r)
#     if q == 6:
#         print("you lose")
#         break
#     c=0
# if q != 6:
#     print("You win")

import random
import os
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = [
    "Snow White and the Seven Dwarfs",
    "Cinderella",
    "Sleeping Beauty",
    "Beauty and the Beast",
    "The Little Mermaid",
    "Aladdin",
    "The Lion King",
    "Pocahontas",
    "Mulan",
    "Tarzan",
    "The Princess and the Frog",
    "Tangled",
    "Frozen",
    "Moana",
    "Brave",
    "Ratatouille",
    "Finding Nemo",
    "Toy Story",
    "Monsters, Inc.",
    "Cars",
    "Up",
    "Inside Out",
    "Coco",
    "Zootopia",
    "The Incredibles",
    "Finding Dory",
    "Wreck-It Ralph",
    "Big Hero 6",
    "Frozen II",
    "The Jungle Book",
    "Alice in Wonderland",
    "Peter Pan",
    "The Hunchback of Notre Dame",
    "Hercules",
    "Hunchback of Notre Dame",
    "Atlantis: The Lost Empire",
    "Treasure Planet",
    "The Emperor's New Groove",
    "The Sword in the Stone",
    "Robin Hood",
    "The Black Cauldron",
    "The Great Mouse Detective",
    "Oliver & Company",
    "The Little Mermaid II: Return to the Sea",
    "Beauty and the Beast: The Enchanted Christmas",
    "Aladdin and the King of Thieves",
    "Pocahontas II: Journey to a New World",
    "The Lion King II: Simba's Pride",
    "Mulan II",
    "The Princess and the Frog",
    "Tangled: Before Ever After",
    "Cars 2",
    "Monsters University",
    "Toy Story 2",
    "Toy Story 3",
    "Ratatouille",
    "WALL-E",
    "Brave",
    "Inside Out",
    "The Good Dinosaur",
    "Finding Dory",
    "Cars 3",
    "Incredibles 2",
    "Frozen II",
    "Soul",
    "Luca",
    "Raya and the Last Dragon",
    "The Little Mermaid (live-action)",
    "Cruella",
    "Jungle Cruise",
    "Peter Pan & Wendy",
    "Aladdin and the Arabian Nights",
    "The Lion King (live-action)",
    "Mulan (live-action)",
    "Beauty and the Beast (live-action)",
    "Dumbo (live-action)",
    "Christopher Robin",
    "Mary Poppins Returns",
    "Maleficent",
    "Maleficent: Mistress of Evil",
    "Oz the Great and Powerful",
    "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe",
    "The Chronicles of Narnia: Prince Caspian",
    "The Chronicles of Narnia: The Voyage of the Dawn Treader",
    "Pirates of the Caribbean: The Curse of the Black Pearl",
    "Pirates of the Caribbean: Dead Man's Chest",
    "Pirates of the Caribbean: At World's End",
    "Pirates of the Caribbean: On Stranger Tides",
    "Pirates of the Caribbean: Dead Men Tell No Tales",
    "National Treasure",
    "National Treasure: Book of Secrets",
    "Enchanted",
    "The Princess Diaries",
    "The Princess Diaries 2: Royal Engagement"]
word = word_list[random.randint(0, 2)]
p = word
p = p.lower()
r=['_']*len(word)
c,q = 0,6
while r!=list(word):
    guess = input("Guess a letter\n")
    os.system('cls')
    for i in range(len(p)):
        if p[i] == guess:
            c += 1
            r[i]=p[i]
    if c >= 1:
        print(f"The letter is present {c} times")
    else:
        print(f"The letter is not present, you have {q-1} lives remaining")
        q -= 1
    print(r)
    print(stages[q])
    if q == 0:
        print("you lose")
        break
    c=0
if q != 0:
    print("You win")