def solution(lst):
    total = 0
    for index in range(len(lst)):
        x = lst[index]
        if index % 2 == 0 and x % 2 == 1:
            total += x
    return total