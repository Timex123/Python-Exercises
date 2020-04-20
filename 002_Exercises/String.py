string = input("put any string: ")
palindrome = string[::-1]
print(palindrome)
print(string)
i = len(string)
print(i)
if palindrome == string:
    print(string + " Ais a palindrome")
else:
    print(string + " is not a palindrome")

