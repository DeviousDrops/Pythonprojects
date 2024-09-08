# print(len("Howdy"))
# print("lmao"[2])
# num=len("bleh")
# print("L"+str(num))
# print(type(num))
# L=input()
# L=L+70
# print(L)
# print(round(10/4,3))
# M=90
# uWinnin=True
# print(f"tf M is {M}?!?!!?!? So its {uWinnin}...")
Bill=float(input("What was the total amount?"))
num_people=float(input("How many of you are splitting the bill?"))
tip=float(input("How much % will u tip?"))
amt_for_each_person=Bill/num_people*(1+tip/100)
amt="{:.2f}".format(amt_for_each_person)
print(f"each person should pay ${amt}")
