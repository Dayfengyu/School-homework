while True:
    s = input("輸入身分證字號:")
    a = 0
    num = 0
    if s[0] == 'A':
        a = 10
    if s[0] == 'B':
        a = 11
    if s[0] == 'C':
        a = 12
    if s[0] == 'D':
        a = 13
    if s[0] == 'E':
        a = 14
    if s[0] == 'F':
        a = 15
    if s[0] == 'G':
        a = 16
    if s[0] == 'H':
        a = 17
    if s[0] == 'I':
        a = 34
    if s[0] == 'J':
        a = 18
    if s[0] == 'K':
        a = 19
    if s[0] == 'L':
        a = 20
    if s[0] == 'M':
        a = 21
    if s[0] == 'N':
        a = 22
    if s[0] == 'O':
        a = 35
    if s[0] == 'P':
        a = 23
    if s[0] == 'Q':
        a = 24
    if s[0] == 'R':
        a = 25
    if s[0] == 'S':
        a = 26
    if s[0] == 'T':
        a = 27
    if s[0] == 'U':
        a = 28
    if s[0] == 'V':
        a = 29
    if s[0] == 'W':
        a = 32
    if s[0] == 'X':
        a = 30
    if s[0] == 'Y':
        a = 31
    if s[0] == 'Z':
        a = 33

    sum = (a//10)+(a % 10)*9
    for i in range(8):
        sum += int(s[i+1])*(8-i)
    sum += int(s[9])
    if sum % 10 == 0:
        print("Valid ID!")
    else:
        print("Invalid ID")
    break