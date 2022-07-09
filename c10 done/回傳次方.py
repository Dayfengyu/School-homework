def rpower(m, n):
    if(n == 0):
        return 1
    elif (m == 0 and n != 0):
        return 0
    else:
        return m*rpower(m, n-1)


a = int(input("a=?"))
b = int(input("b=?"))
print("The %d-th power of %d is %d." % (b, a, rpower(a, b)))
