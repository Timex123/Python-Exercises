Len = int(input("Length of the board? Len: "))
Wid = int(input("width of the board? Wid: "))
print("The board will be: ", Len, " x ", Wid)
Dots = " ---"
Line = "|   "

def print_Line():
    print((Len+1)*Line)

def print_Dots():
    print((Len)*Dots)


i = 0
while i < Wid:
    print_Dots()
    print_Line()
    i = i + 1
print_Dots()


