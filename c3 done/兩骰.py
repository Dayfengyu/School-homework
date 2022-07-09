import random

a = random.randint(0, 6)+1
b = random.randint(0, 6)+1

if a > b:
    c = a 
    a = b
    b = c

print("Throwing two dice ... ")

print("One dice shows %d and the other dice shows %d." % (a, b))

print("The total score is %d + %d = %d." % (a, b, a+b))
