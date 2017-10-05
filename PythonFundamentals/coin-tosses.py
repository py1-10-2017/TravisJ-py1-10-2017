def coinToss(times):
    import random

    tails = 0
    heads = 0

    for i in range(1, times + 1):
        x = random.random()
        if(round(x) == 1):
            heads += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
        else:
            tails += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a tail! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"


coinToss(5000)
