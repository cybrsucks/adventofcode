# this is one game
# A, X
# B, Y
# C, Z

# this is one round (e.g. first round)
# A, X

# this is another round (e.g. second round)
# B, Y

# A ROCK 1
# B PAPER 2
# C SCISSORS 3

# X PAPER 2
# Y SCISSORS 3
# Z ROCK 1

# POINTS SYSTEM
rock = 1
paper = 2
scissors = 3

loss = 0
draw = 3
win = 6

import os
import sys

file = open(os.path.join(sys.path[0], "game_1.txt"), "r")   # 3 win streak
file2 = open(os.path.join(sys.path[0], "game_2.txt"), "r")   # in the event of a tie


files = [file, file2]   # variation of file input

A = Z = 1   # rock
B = X = 2   # paper
C = Y = 3   # scissors

for f in files:   # loop thru file variations
    game = f.readlines()
    count = 0

    for g in game:
        count += 1   # round number
        roundN = g.strip()   # roundN prints A, X    # B, Y
        roundN_play = roundN.split(', ')   # splits values at comma into list
        # print(roundN_play)
        x = 0
        for shape in roundN_play:
            x += 1   # player 1 = opponent, player 2 = my play
            print("Round Number: ({}), Player {} plays {}".format(count, x, shape))
        print("End of round\n")

    print("end of file\n")

