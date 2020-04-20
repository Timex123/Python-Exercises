import random
from random import choice
from string import ascii_lowercase

print("How strong do you want your password?")
print("1 - low "
      "2 - middle "
      "3 - strong")
number = int(input("I pick: "))

hasla = open('hasla.txt').read().split()
print(hasla)

if number == 1:
    password = random.choice(hasla)      # hasla[random.randint(0,len(hasla)-1)]
    print(password)

if number == 2:
    n = 10
    password = "".join(choice(ascii_lowercase) for i in range(n))
    print(password)

if number == 3:
    s = "abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ123456890!@#$%^&*()"
    n = 15
    password = "".join(random.sample(s,n))
    print(password)
