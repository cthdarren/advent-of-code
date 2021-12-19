with open("adventofcode.txt") as file:
    fishList = [int(x) for x in file.readline().rsplit()[0].split(",")]

days = 256
fishDict = {}
for x in range(9):
    fishDict[str(x)] = fishList.count(x)

for x in range(days):
    oldZero = fishDict['0']
    for y in range(6):
        fishDict[str(y)] = fishDict[str(y+1)]
    fishDict['6'] = fishDict['7'] + oldZero
    fishDict['7'] = fishDict['8']
    fishDict['8'] = oldZero
print(sum(fishDict.values()))
