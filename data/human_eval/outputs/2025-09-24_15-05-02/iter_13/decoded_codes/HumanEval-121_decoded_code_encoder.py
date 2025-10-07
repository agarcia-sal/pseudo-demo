def solution(lst):
    result = 0
    for idx in range(len(lst)):
        if idx % 2 == 0 and lst[idx] % 2 == 1:
            result += lst[idx]
    return result