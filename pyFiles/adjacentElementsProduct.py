def solution(inputArray):
    for i in range(len(inputArray) - 1):
        testVal = inputArray[i] * inputArray[i+1]
        if i == 0:
            biggestVal = testVal
        elif testVal > biggestVal:
            biggestVal = testVal
    return biggestVal