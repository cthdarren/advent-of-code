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
    lineList.append([startList[index], endList[index]])

for coordSet in lineList:
    startCoord = coordSet[0]
    endCoord = coordSet[1]

    if startCoord[0] == endCoord[0]:
        minCoord = min(startCoord[1],endCoord[1])
        maxCoord = max(startCoord[1],endCoord[1])

        for value in range(minCoord, maxCoord + 1):
            coordList.append(str(startCoord[0]) + "," + str(value))

    elif startCoord[1] == endCoord[1]:
        minCoord = min(startCoord[0],endCoord[0])
        maxCoord = max(startCoord[0],endCoord[0])

        for value in range(minCoord, maxCoord + 1):
            coordList.append(str(value) + "," + str(startCoord[1]))
    else:
        minCoord = min(startCoord[0],endCoord[0])
        maxCoord = max(startCoord[0],endCoord[0])
        count = 0
        if startCoord[0] > endCoord[0]:
            if startCoord[1] > endCoord[1]:
                for x in range(minCoord, maxCoord + 1):
                    coordList.append(str(startCoord[0]-count) + "," + str(startCoord[1]-count))
                    count += 1
            elif startCoord[1] < endCoord[1]:
                for x in range(minCoord, maxCoord + 1):
                    coordList.append(str(startCoord[0]-count) + "," + str(startCoord[1]+count))
                    count += 1
        else:
            if startCoord[1] > endCoord[1]:
                for x in range(minCoord, maxCoord + 1):
                    coordList.append(str(startCoord[0]+count) + "," + str(startCoord[1]-count))
                    count += 1
            elif startCoord[1] < endCoord[1]:
                for x in range(minCoord, maxCoord + 1):
                    coordList.append(str(startCoord[0]+count) + "," + str(startCoord[1]+count))
                    count += 1

seen = set()
dupes = []
for x in coordList:
    if x in seen and x not in dupes:
        dupes.append(x)
    else:
        seen.add(x)

print(len(dupes))