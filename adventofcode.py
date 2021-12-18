
def returnBoard():
    numbers = [18,99,39,89,0,40,52,72,61,77,69,51,30,83,20,65,93,88,29,22,14,82,53,41,76,79,46,78,56,57,24,36,38,11,50,1,19,26,70,4,54,3,84,33,15,21,9,58,64,85,10,66,17,43,31,27,2,5,95,96,16,97,12,34,74,67,86,23,49,8,59,45,68,91,25,48,13,28,81,94,92,42,7,37,75,32,6,60,63,35,62,98,90,47,87,73,44,71,55,80]

    boards = [[]]
    lastBoard = False
    with open("adventofcode.txt") as file:
        numbers = file.readline().rstrip().split(",")
        file.readline()
        count = 0
        for line in file:
            if line != "\n":
                boards[count].append(line.split())
            else:
                boards.append([])
                count += 1

    for num in numbers:
        boards = [x for x in boards if x != 0]
        for index, board in enumerate(boards):
            if len(boards) == 1:
                lastBoard = True
            commonColumns = []
            firstRow = True
            for row in board:                    
                rowcolumn = []
                if num in row:
                    row[row.index(num)] = "X"
                if row.count("X") == 5:
                    if lastBoard:
                        return board, num
                    boards[index] = 0
                elif "X" in row:
                    for i,x in enumerate(row):
                        if firstRow:
                            if x == "X":
                                commonColumns.append(i)
                        else:
                            if x == "X":
                                rowcolumn.append(i)
                if not firstRow:
                    if any(x in rowcolumn for x in commonColumns):
                        tempColumn = commonColumns
                        commonColumns = []
                        for val in tempColumn:
                            if val in rowcolumn:
                                commonColumns.append(val)
                    else:
                        commonColumns = []
                if firstRow:
                    firstRow = False
            if len(commonColumns) > 0:
                if lastBoard:
                    return board, num
                boards[index] = 0

board, num = returnBoard()

result = 0
for row in board:
    for values in row:
        if values != "X":
            result += int(values)

print(result * int(num))
