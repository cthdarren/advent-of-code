with open("adventofcode.txt") as file:
    fishList = [int(x) for x in file.readline().rsplit()[0].split(",")]

days = 80

for x in range(days):
    newFishCount = 0
    for index, fish in enumerate(fishList):
        newFish = fish - 1
        if fish == 0:
            newFishCount += 1
        if fish < 7:
            fishList[index] = newFish%7
        else:
            fishList[index] = newFish
    for x in range(newFishCount):
        fishList.append(8)

    # print("Day " + str(x + 1) + ":")
print(len(fishList))
        