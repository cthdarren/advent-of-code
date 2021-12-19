with open("adventofcode.txt") as file:
    numberList = [int(x) for x in file.readline().split(",")]

numberList.sort()

minFuel = numberList[499]

totalFuel = 0
for number in numberList:
    totalFuel += abs(328-number)

print(totalFuel)