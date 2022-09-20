def solution(inputString):
    if inputString[::-1] == inputString:
        return True
    else:
        return False