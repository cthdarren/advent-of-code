outputList = []
cipherList = []
count = 0
totalResult = 0
with open("adventofcode.txt") as file:
    for line in file:
        sortedInput = []
        sortedOutput = []
        inputOutput = line.split("|")
        inputOutput[0] = inputOutput[0].rsplit()
        inputOutput[1] = inputOutput[1].rsplit()

        for x in inputOutput[0]:
            sortedInput.append("".join(sorted(x)))
        for y in inputOutput[1]:
            sortedOutput.append("".join(sorted(y)))
        outputList.append([sortedInput, sortedOutput])


for entry in outputList:
    result = ""
    cipher = entry[0]
    output = entry[1]
    decipherDict = {str(x):None for x in range(10)}
    decipherDict["4"] = [x for x in cipher if len(x) == 4][0]
    decipherDict["8"] = [x for x in cipher if len(x) == 7][0]
    decipherDict["7"] = [x for x in cipher if len(x) == 3][0]
    decipherDict["1"] = [x for x in cipher if len(x) == 2][0]
    for string in cipher:
        if len(string) == 5:
            if decipherDict["1"][0] in string and decipherDict["1"][1] in string:
                decipherDict["3"] = string
            else:
                count = 0
                for x in string:
                    if x in decipherDict["4"]:
                        count += 1
                if count == 3:
                    decipherDict["5"] = string
                else:
                    decipherDict["2"] = string
        elif len(string) == 6:
            if decipherDict["4"][0] in string and decipherDict["4"][1] in string and decipherDict["4"][2] in string and decipherDict["4"][3] in string:
                decipherDict["9"] = string
            else:
                if decipherDict["7"][0] in string and decipherDict["7"][1] in string and decipherDict["7"][2] in string:
                    decipherDict["0"] = string
                else:
                    decipherDict["6"] = string
    
    resDict = dict((v,k) for k,v in decipherDict.items())
    for string in output:
        result += str(resDict[string])
    totalResult+= int(result)

print(totalResult)