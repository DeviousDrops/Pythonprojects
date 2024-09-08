import random
def generator():
    numbers=['ace',2,3,4,5,6,7,8,9,10,'king','queen','jack']
    return random.choice(numbers)

def calc(l):
    s=0
    for i in l:
        if i=='ace':
            if s<11:
                s+=11
            else:
                s+=1
        elif i=='king' or i=='queen' or i=='jack':
            s+=10
        else:
            s+=i
    return s


print("Dealer hands you two cards and the computer 2 cards")
human=[generator(),generator()]
comp=[generator(),generator()]
hscore=calc(human)
cscore=calc(comp)
while cscore<= 10:
    comp.append(generator())
    cscore=calc(comp)
while True:
    print(f"your hand: \n{human} \nscore: {hscore}")
    temp=comp
    temp.pop()
    print(f"opponent's hand excluding the last card: \n{temp}")
    f=input("Do you want to draw another card? Type y/n for yes or no?:\n")
    if f=='n':
        break
    human.append(generator())
    hscore=calc(human)
    if hscore>21:
        print(f"hand: \n{human} \nscore: {hscore}\nYou bust")
        exit()
print(f"your hand: \n{human} \nscore: {hscore}")
print(f"opponent's hand: \n{comp} \nscore: {cscore}")
if hscore==cscore:
    print('draw')
elif hscore>cscore:
    print('you win')
else:
    print('you lose')



    

    

    
