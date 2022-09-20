def solution(n):
    area = 1
    while n > 0:
        n -= 1
        area += 4 * n
    return area