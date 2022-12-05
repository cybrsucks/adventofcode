import os
import sys

file = open(os.path.join(sys.path[0], "elf_on_a_shelf.txt"), "r")
file2 = open(os.path.join(sys.path[0], "elf_on_a_shelf_2.txt"), "r")

files = [file, file2]   # variation of file input

for f in files:   # loop thru file variations

    lines = f.readlines()
    # print(lines)

    elf = 0
    elves_total = []

    count = 0
    for line in lines:

        if line.strip():    # checks if line in file contains any text
            elf += int(line)
            # print(elf)

        else:   # empty line, separate
            # print("boom")
            elves_total.append(elf)
            elf = 0
            # print(elves_total)

    elves_total.append(elf)   # append last elf

    elf_max = elves_total.index(max(elves_total)) + 1
    elf_max_total = max(elves_total)
    print("Elf carrying the most Calories: {} ".format(elf_max))
    print("Total amount of calories the Elf is carrying: {} ".format(elf_max_total))

