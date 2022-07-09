eng = ["zero", "one", "two", "three", "four",
       "five", "six", "seven", "eight", "nine"]

while 1:
    inp = input("阿拉伯數字：")
    if(inp >= '0' and inp <= '9'):
        print(str(eng[int(inp)]))
    elif(inp == 'Q' or inp == 'q'):
        print("bye!")
        break
    else:
        print("Wrong! Try Again!")
