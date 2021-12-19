import math, sys
with open("adventofcode.txt") as file:
    numberList = [int(x) for x in file.readline().split(",")]

totalFuel = sys.maxsize

for x in range(max(numberList)):
    temp = 0
    for number in numberList:
        temp += (abs(x-number)/2)*(1+abs(x-number))
    if temp < totalFuel:
        totalFuel = temp
        
print(totalFuel)

