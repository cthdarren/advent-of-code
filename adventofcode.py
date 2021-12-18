binaries = list()
with open("adventofcode.txt") as file:
    for line in file:
        binaries.append(str(line.rstrip()))

def returnBitList(list, index, mostCommon):
    oneList = []
    zeroList = []
    for b in list:
        if b[index] == '1':
            oneList.append(b)
        else:
            zeroList.append(b)
    
    if mostCommon == True:
        if not len(oneList):
            return zeroList
        if not len(zeroList):
            return oneList

        if len(oneList) > len(zeroList):
            return oneList
        elif len(oneList) == len(zeroList):
            return oneList
        return zeroList
    else:
        if not len(oneList):
            return zeroList
        if not len(zeroList):
            return oneList
            
        if len(oneList) > len(zeroList):
            return zeroList
        elif len(oneList) == len(zeroList):
            return zeroList
        return oneList

oxygenresult = returnBitList(binaries,0, True)
for x in range(1,len(binaries[0])):
    oxygenresult = returnBitList(oxygenresult, x, True)

co2result = returnBitList(binaries,0, False)
for x in range(1,len(binaries[0])):
    co2result = returnBitList(co2result, x, False)

print(oxygenresult)
print(co2result)
print(int(oxygenresult[0], 2) * int(co2result[0], 2))