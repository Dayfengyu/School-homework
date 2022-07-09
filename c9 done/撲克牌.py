import random

a = ['♥', '♠', '♦', '♣']
b = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
card = []

for i in range(52):
    card.append(i)

for i in range(100):
    z = random.randint(0, 51)
    temp = card[i % 52]
    card[i % 52] = card[z]
    card[z] = temp

for i in range(1, 53):
    print(a[int(card[i-1]/13)], (b[int(card[i-1] % 13)]), end='  ')
    if(i % 13 == 0):
        print("\n")
