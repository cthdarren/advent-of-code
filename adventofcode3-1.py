import math

firstline = None
lenfile = 0
gamma = ""
epsilon = ""
with open("adventofcode.txt") as file:
    for line in file:
        if firstline == None:
            firstline = line
            count = [0] * len(firstline.rstrip())

        for i,char in enumerate(line):
            if char == '1':
                count[i] += 1
        lenfile += 1

    for x in count:
        if x > lenfile/2:
            epsilon += "0"
            gamma += "1"
        else:
            epsilon += "1"
            gamma += "0"

    print(int(epsilon,2) * int(gamma,2))