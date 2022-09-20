def solution(year):
    century = 0
    if year > 1000:
        year -= 1000
        century = 10
    while (year > 0):
        year -= 100
        century += 1
    return century