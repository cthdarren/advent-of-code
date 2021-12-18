xvalue = 0
yvalue = 0
aim = 0
with open("adventofcode.txt") as file:
    for line in file:
        if "forward" in line:
            xvalue += int(line.replace("forward","").strip())
            yvalue += aim * int(line.replace("forward","").strip())
        elif "up" in line:
            aim -= int(line.replace("up","").strip())
        elif "down" in line:
            aim += int(line.replace("down","").strip())

    print(xvalue * yvalue)