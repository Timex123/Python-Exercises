string = "I want to split this"
split = string.split()
print(split)
print(len(split))
split_reversed = split[::-1]
print(split_reversed)
string_reversed = " ".join(split_reversed)
print(string_reversed)