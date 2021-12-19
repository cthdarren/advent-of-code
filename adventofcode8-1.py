outputList = []
count = 0
with open("adventofcode.txt") as file:
    for line in file:
        output = line.split("|")[1].rsplit()
        for x in output:
            outputList.append(x)

for x in outputList:
    if  2 <= len(x) <= 4 or len(x) == 7:
        count +=1 

print(count)