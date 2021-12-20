largest = []
area = []
lowPoints = []
result = 0
with open("adventofcode.txt") as file:
    for line in file:
        area.append([int(number) for number in line.rstrip()])

for y, row in enumerate(area):
    for x, number in enumerate(row):
        if y == 0:
            if x == 0:
                if number < area[y+1][x] and number < area[y][x+1]:
                    lowPoints.append([y,x])
                    result += number + 1
            elif x == len(row) -1:
                if number < area[y+1][x] and number < area[y][x-1]:
                    lowPoints.append([y,x])
                    result += number + 1
            else:
                if number < area[y+1][x] and number < area[y][x-1] and number < area[y][x+1]:
                    lowPoints.append([y,x])
                    result += number + 1

        elif y == len(area) -1:
            if x == 0:
                if number < area[y-1][x] and number < area[y][x+1]:
                    lowPoints.append([y,x])
                    result += number + 1
            elif x == len(row) -1:
                if number < area[y-1][x] and number < area[y][x-1]:
                    lowPoints.append([y,x])
                    result += number + 1
            else:
                if number < area[y-1][x] and number < area[y][x-1] and number < area[y][x+1]:
                    lowPoints.append([y,x])
                    result += number + 1

        elif len(row)-1 > x > 1 and len(area) -1 > y > 1:
            if number < area[y-1][x] and number < area[y+1][x] and number < area[y][x+1] and number < area[y][x-1]:
                lowPoints.append([y,x])
                result += number + 1
        
print(len(lowPoints))
print(result)