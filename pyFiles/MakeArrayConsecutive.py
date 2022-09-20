def solution(statues):
    numStatuesNeed = 0
    newList = []
    while len(statues) > 0:
        testVal = 100
        for i in range(len(statues)):
            if testVal > statues[i]:
                testVal = statues[i]
        newList.append(testVal)
        statues.remove(testVal)
    for i in range(len(newList)-1):
        val1 = newList[i]
        val2 = newList[i+1]
        while val2 - val1 > 1:
            val2 -= 1
            numStatuesNeed += 1
    return numStatuesNeed