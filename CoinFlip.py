import random

def flipCoin(numberOfFlips):
    tails=0
    heads=0

    for i in range(numberOfFlips):
        rand=random.randint(1,2)
        if rand==1:
            tails+=1
            print("tails")
        else:
            heads+=1
            print("heads")

    print("heads: ", heads)
    print("tails: " , tails)

    print("heads: ", heads/numberOfFlips*100,"%")
    print("tails: ", tails/ numberOfFlips * 100,"%")


flipTimes=int(input("how many coins do you want to flip?"))
flipCoin(flipTimes)

input('Press ENTER to exit') 