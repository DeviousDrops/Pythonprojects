# def greet():
#     print('Hello world!')
# greet()
import os
os.system('cls')
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(msg,sh):
    ciph=''
    for i in msg:
        if i.isalpha():
            ciph+=chr((sh+ord(i)-97)%25 + 97)
        else:
            ciph+=i
    print('encrypted msg = '+ciph)
def decrypt(msg,sh):
    ciph=''
    for i in msg:
        if i.isalpha():
            if ord(i)-sh<=97:
                ciph+=chr(122+(ord(i)-sh-97))
            else:
                ciph+=chr((ord(i)-sh-97)%25 + 97)
        else:
            ciph+=i
    print('decrypted msg = '+ciph)
if direction=='encode':
    encrypt(text,shift)
elif direction=='decode':
    decrypt(text,shift)            