areaList = []
result = 0
with open("adventofcode.txt") as file:
    for line in file:
        areaList.append(line.rstrip())

def isLowPoint(index, currentRow, nextRow = None, previousRow = None):
    if index != 0:
        if int(currentRow[index-1]) <= int(currentRow[index]):
            return False
    if index != len(currentRow) -1:
        if int(currentRow[index+1]) <= int(currentRow[index]):
            return False
    if nextRow:
        if int(nextRow[index]) <= int(currentRow[index]):
            return False
    if previousRow:
        if int(previousRow[index]) <= int(currentRow[index]):
            return False
    return True

for rowIndex, row in enumerate(areaList):
    for index, point in enumerate(row):
        if rowIndex == 0 and len(areaList) > 1:
            if isLowPoint(index, row, areaList[rowIndex+1]):
                result += 1 + int(point)
        elif rowIndex == len(areaList)-1:
            if isLowPoint(index, row, None, areaList[rowIndex-1]):
                result += 1 + int(point)
        else:
            if isLowPoint(index, row, areaList[rowIndex+1], areaList[rowIndex-1]):
                result += 1 + int(point)
print(result)