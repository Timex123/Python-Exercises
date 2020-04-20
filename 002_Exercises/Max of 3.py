print("Input 3 variables: ")
variables = input()
print(variables)
list = variables.strip().split(" ")
print(list)

for i in range(0, len(list)):
    list[i] = int(list[i])
print(list)

if list[0] > list[1]:
    if list[0] > list[2]:
        print(list[0])
    else:
        print(list[2])

else:
    if list[1] > list[2]:
        print(list[1])
    else:
        print(list[2])

print("Max is:", max(list))