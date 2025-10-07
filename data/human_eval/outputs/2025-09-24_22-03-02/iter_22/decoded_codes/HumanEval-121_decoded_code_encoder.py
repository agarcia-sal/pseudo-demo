def solution(lst):
    total = 0
    index = 0
    while index < len(lst):
        x = lst[index]
        if (index % 2 == 0) and (x % 2 == 1):
            total += x
        index += 1
    return total