# this is one game
# A, X
# B, Y
# C, Z

# this is one round (e.g. first round)
# A, X

# this is another round (e.g. second round)
# B, Y

import os
import sys

file = open(os.path.join(sys.path[0], "game_1.txt"), "r")   # 3 win streak
file2 = open(os.path.join(sys.path[0], "game_2.txt"), "r")   # in the event of a tie
# file3 = open(os.path.join(sys.path[0], "game_3.txt"), "r")   # all possible outcomes

files = [file, file2]   # variation of file input
# files = [file, file2, file3]   # variation of file input

# values of rock, paper, scissors
shapes = {
    "A": 1,
    "Z": 1,
    "B": 2,
    "X": 2,
    "C": 3,
    "Y": 3
}

# shape = shapes["A"]
# print(shape)

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
        print("Round " + str(count))
        for shape in roundN_play:
            x += 1   # player 1 = opponent, player 2 = my play
            print("Player {} plays {}".format(x, shape))
            valList.append(shapes[shape])   # get value of ABCXYZ from dict
            # print("shapeVal: {}".format(shapeVal))
        print(valList)
        if (valList[0] == 3) & (valList[1] == 1):   # special condition specified in Line 50-52
            me += valList[1] + 6
            # print("I win this round")
        elif (valList[0] == 1) & (valList[1] == 3):   # special condition specified in Line 50-52
            opponent += valList[0] + 6
            # print("Opponent wins this round")
        elif valList[0] < valList[1]:   # I win this round
            me += valList[1] + 6
            # print("I win this round")
        elif valList[0] == valList[1]:   # Tie round
            me += valList[1] + 3
            opponent += valList[0] + 3
            # print("Tied round")
        else:
            opponent += valList[0] + 6
            # print("Opponent wins this round")
        print("My points: {}".format(me))
        print("Opponent points: {}".format(opponent))
        print("End of round\n")
    print("end of file\n")
