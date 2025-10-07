def solution(lst):
    result = 0
    for idx in range(len(lst)):
        x = lst[idx]
        if idx % 2 == 0 and x % 2 == 1:
            result += x
    return result