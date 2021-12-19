startList = []
endList = []
lineList = []
coordList = []

with open("adventofcode.txt") as file:
    for line in file:
        coords = line.replace("\n","").split("->")
        startList.append([int(x) for x in coords[0].split(",")])
        endList.append([int(x) for x in coords[1].split(",")])

for index in range(len(startList)):
    if startList[index][0] == endList[index][0] or startList[index][1] == endList[index][1]:
        lineList.append([startList[index], endList[index]])

for coordSet in lineList:
    xCoord = coordSet[0]
    yCoord = coordSet[1]
    if xCoord[0] == yCoord[0]:
        minCoord = min(xCoord[1],yCoord[1])
        maxCoord = max(xCoord[1],yCoord[1])
        for value in range(minCoord, maxCoord + 1):
            coordList.append(str(xCoord[0]) + "," + str(value))
    elif xCoord[1] == yCoord[1]:
        minCoord = min(xCoord[0],yCoord[0])
        maxCoord = max(xCoord[0],yCoord[0])
        for value in range(minCoord, maxCoord + 1):
            coordList.append(str(value) + "," + str(xCoord[1]))

seen = set()
dupes = []
for x in coordList:
    if x in seen and x not in dupes:
        dupes.append(x)
    else:
        seen.add(x)

print(len(dupes))