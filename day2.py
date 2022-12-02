# how many combinations are there?
# A for Rock, B for Paper, and C for Scissors. -> opponent
# X for Rock, Y for Paper, and Z for Scissors. -> yours
# Your total score is the sum of your scores for each round. 
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
scoreList = []
def score(opponentShape, yourShape):
    listopponentShape = {"A": 1, "B": 2, "C": 3}
    listyourShape = {"X": 1, "Y": 2, "Z": 3}
    yourShape2 = listyourShape[yourShape]
    opponentShape2 = listopponentShape[opponentShape]
    def winCondition():
        if yourShape2 == 1 and opponentShape2 == 3:
            return 6
        elif yourShape2 == 3 and opponentShape2 == 1:
            return 0
        else:
            if yourShape2 > opponentShape2:
                return 6
            elif yourShape2 == opponentShape2:
                return 3
            else:
                return 0 # lost
    
    totalScore = winCondition() + int(yourShape2)
    scoreList.append(totalScore)
    
    
with open('day2input.txt', 'r') as readline:
    for line in readline:
        test = line.split()
        score(test[0], test[1])
        # score(readline.read(1), line.strip()[1::1]) # run score() with the third character of each line being passed as argument           
print(sum(scoreList))

#part 2
# X means lose, Y means draw, Z means win.
# A for Rock, B for Paper, and C for Scissors. -> opponent

scoreList = []

def score2(opponentShape, doiwin):
    listopponentShape = {"A": 1, "B": 2, "C": 3}
    listdoiwin = {"X": 0, "Y": 3, "Z": 6}
    opponentShape2 = listopponentShape[opponentShape]
    doiwin2 = listdoiwin[doiwin]    

    def winorlose():
        if doiwin2 == 0:
            if opponentShape2 == 1:
                yourshape = 3
            else:
                yourshape = opponentShape2 - 1
        elif doiwin2 == 3:
            yourshape = opponentShape2
        else:
            if opponentShape2 == 3:
                yourshape = 1
            else:
                yourshape = opponentShape2 + 1
        return yourshape
        
    scoreList.append(doiwin2 + winorlose())
    

with open('day2input.txt', 'r') as readline:
    for line in readline:
        test = line.split()
        score2(test[0], test[1])

print(sum(scoreList))