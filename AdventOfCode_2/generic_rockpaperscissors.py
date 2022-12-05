# this is one game
# rock, paper
# paper, scissors
# scissors, rock

# this is one round (e.g. first round)
# rock, paper

# this is another round (e.g. second round)
# paper, scissors

import os
import sys

file = open(os.path.join(sys.path[0], "game_3.txt"), "r")   # 3 win streak

files = [file]   # variation of file input

# values of rock, paper, scissors
shapes = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

# we will use if OppShape < MyShape to determine if I win or lose, exception being:
# if OppShape = C (scissors), MyShape = Z (rock), then I win.
# if OppShape = A (rock), MyShape = Y (scissors), then I lose.
# Since the dictionary value indicated is lower, this is to be hard coded

for f in files:   # loop thru file variations
    game = f.readlines()
    count = 0

    # init values before games
    opponent = 0
    me = 0

    for g in game:
        count += 1   # round number
        roundN = g.strip()   # roundN prints A, X    # B, Y
        roundN_play = roundN.split(', ')   # splits values at comma into list
        # print(roundN_play)
        x = 0
        valList = []
        for shape in roundN_play:
            x += 1   # player 1 = opponent, player 2 = my play
            print("Round Number: ({}), Player {} plays {}".format(count, x, shape))
            valList.append(shapes[shape])
            # print("shapeVal: {}".format(shapeVal))
        print(valList)
        if (valList[0] == 3) & (valList[1] == 1):   # special condition specified in Line 50-52
            me += valList[1] + 6
            print("I win this round")
        elif (valList[0] == 1) & (valList[1] == 3):   # special condition specified in Line 50-52
            opponent += valList[0] + 6
            print("Opponent wins this round")
        elif valList[0] < valList[1]:   # I win this round
            me += valList[1] + 6
            print("I win this round")
        elif valList[0] == valList[1]:   # Tie round
            me += valList[1] + 3
            opponent += valList[0] + 3
            print("Tied round")
        else:
            opponent += valList[0] + 6
            print("Opponent wins this round")
        print(me)
        print(opponent)
        print("End of round\n")
    print("end of file\n")
