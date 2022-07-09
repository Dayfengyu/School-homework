import random
a = int(input("輸入0~100的整數:"))

if a == 100:
    b = random.randint(0, a)
    print("Your input integer is between %d and 100." % b)
elif a == 0:
    c = random.randint(0, 101)
    print("Your input integer is between 0 and %d." % c)
else:
    b = random.randint(0, a)
    c = random.randint(0, (100-a))+a
    print("Your input integer is between %d and %d.\n" % (b, c))
