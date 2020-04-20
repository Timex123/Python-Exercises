import datetime

name = input("Your name please: ")
print("Your name is " + name)
age = input("Your age is: ")
age = int(age)
now = datetime.datetime.now()
print(now)
StoLat = str(now.year - age + 100)
print("You'll be 100 in: " + StoLat)
