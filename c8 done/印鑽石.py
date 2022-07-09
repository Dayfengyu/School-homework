i = int(input("鑽石階層?:"))

for a in range(1, 2*i, 1):
    if(a <= i):
        for b in range(i, a, -1):
            print(" ", end=' ')
        print("*", end=' ')
        for c in range(1, 2*a-2, 1):

            print(" ", end=' ')
        if(a > 1):
            print("*", end=' ')
    else:
        for b in range(a, i, -1):
            print(" ", end=' ')
        print("*", end=' ')
        for c in range(1, (4*i-2*a)-2, 1):
            print(" ", end=' ')
        if(a < (2*i-1)):
            print("*", end=' ')
    print("\n")
