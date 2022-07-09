a, b, c, s = 0, 0, 0, 0
while 1:

    n = int(input("Please input a number: "))
    if(n < 2):
        print("Your input number must be higher than 2!")
        continue
    for a in range(2, n+1):
        if(a == 2):
            print("%dx%d" % (a+1, a-1), end='')
        else:
            print("+%dx%d" % (a+1, a-1), end='')
    print("=", end='')
    for b in range(2, n+1):
        if(b == 2):
            c = (b+1)*(b-1)
            print(c, end='')
        else:
            c = (b+1)*(b-1)
            print("+%d" % c, end='')
        s += c
    print("=%d" % s, end='')
    break
