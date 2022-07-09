import random

card = []
point = ['A', '2', '3', '4', '5', '6', '7', '8',
         '9', 'T', 'J', 'Q', 'K']
money, bet, current, z = 1000, 100, 0, 7
wash = True

print("-------------------------------")
print("Poker Game: Bigger or Smaller?!")
print("-------------------------------")
print("Press h for help.\n")

while True:

    if(bet > money):
        bet = money

    print("[$%d][Bet %d] Cards(%d)" % (money, bet, 52-current))
    cmd = input("Bigger or Smaller than %d (b/s)? " % z)

    if(wash == True):
        for i in range(52):
            card.append(i)
        for i in range(52):
            j = random.randint(0, 52)
            temp = card[i]
            card[i] = j
            j = temp
        wash = False
        current = 0

    if(cmd == 'h'):
        print("h for help")
        print("i for increasing your bet")
        print("d for decreasing your bet")
        print("b for guessing the card is bigger")
        print("s for guessing the card is smaller")
        print("w for re-washing the cards")
        print("q for quit\n")

    elif(cmd == 'i'):
        if(bet == money):
            print("No more money to bet!")
        if(bet+100 <= money):
            bet += 100
        else:
            bet = money

    elif(cmd == 'd'):
        if(bet == 100):
            print("Minimum bet is 100!")
        if(bet >= 200):
            bet -= 100
        else:
            bet = 100

    elif(cmd == 'w'):
        wash = True
        current = 0
        z = 7

    elif(cmd == 'b' or cmd == 's'):
        print("The card is ", end='')

        if(card[current]//13 == 0):
            print('♥' + point[card[current] % 13])
        elif(card[current]//13 == 1):
            print('♠' + point[card[current] % 13])
        elif(card[current]//13 == 2):
            print('♦' + point[card[current] % 13])
        elif(card[current]//13 == 3):
            print('♣' + point[card[current] % 13])

        if(((cmd == 'b') and (card[current] % 13+1 >= z)) or
           ((cmd == 's') and (card[current] % 13+1 <= z))):
            print("You Win!")
            money += bet
        else:
            print("You Lose!")
            money -= bet
        z = card[current] % 13+1
        current += 1

    elif(cmd == 'q'):
        print("Good Bye!")
        break

    else:
        print("Wrong Input!")

    if(money < 100):
        print("Gane Over!")
        break

    if(current == 41):
        wash = True
