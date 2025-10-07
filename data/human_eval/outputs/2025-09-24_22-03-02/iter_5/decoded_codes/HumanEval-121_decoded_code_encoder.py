def solution(lst):
    result = 0
    for index, x in enumerate(lst):
        if index % 2 == 0 and x % 2 == 1:
            result += x
    return result