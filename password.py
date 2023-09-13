import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p','q','r','s','t','u','v','w','x','y','z'
         'A','B','C','D','E','F','G','H','I','J','K','L','M',
         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+','?','@','^']
l=int(input("how many letters you want in your password?:"))
d= int(input("how many digits you want in your password?:"))
s = int(input("how many symbols you want in your password?:"))
password_list=[]
for n in range (1,l+1):
    character=random.choice(letters)
    password_list +=character
for n in range(1, d+ 1):
    character = random.choice(digits)
    password_list += character
for n in range(1, s+ 1):
    character = random.choice(symbols)
    password_list += character
random.shuffle(password_list)
print(password_list)
password=""
for i in password_list:
    password +=i
print(password)



