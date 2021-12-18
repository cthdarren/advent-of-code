
def returnBoard():

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
                    return board, num
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
                return board, num
board, numRoll = returnBoard()

result = 0
for row in board:
    for num in row:
        if num == "X":
            continue
        result += int(num)

print(result*int(numRoll))

