import json
import datetime
from datetime import datetime
from collections import Counter
from bokeh.plotting import figure, show, output_file



##birthdays = {
##  'John': '09/10/1940',
##  'Paul': '18/06/1942',
##  'George': '25/02/1943',
##  'Ringo': '07/07/1940' }

##birthdays['David'] = '06/03/1946'

##with open("Birthdays.json", "w") as f:
##  json.dump(birthdays, f)

with open("Birthdays.json", "r") as f:
  List = json.load(f)

print(List.keys())

name = input("Write a name: ")

print(List[name])

##List['Roger'] = '06/09/43'
##print(List.keys())

print("Do you want to add someone? y/n?")
add = input()

if add == "y":
  name = input("Please give me a name: ")
  date = input("Please give me a date: ")
  List[name] = date
  print(List.keys())

print("Do you want to remove someone? y/n")
remove = input()

if remove == "y":
  name = input("Please give me a name to remove: ")
  List.pop(name)

print(List)
CountMonths = List
Count = []

for x in List:
  Count.append(datetime.strptime(CountMonths[x], "%d/%m/%Y"))

print(List)
print(CountMonths)
print(Count)

i = 0
while i < len(Count):
  Count[i] = Count[i].strftime('%B')
  i = i+1

print(Count)
c = Counter(Count)
print(c)
print(type(Count[0]))

y = []
for item in c:
  y.append(c[item])

Months_Range = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
p = figure()

p = figure(x_range=Months_Range)
p.vbar(x=Count, top=y, width=0.5)

show(p)

with open("Birthdays.json", "w") as f:
  json.dump(List, f)