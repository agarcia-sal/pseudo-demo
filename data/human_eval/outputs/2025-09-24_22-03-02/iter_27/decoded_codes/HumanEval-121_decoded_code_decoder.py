def solution(lst):
    result = 0
    index = 0
    while index < len(lst):
        x = lst[index]
        condition1 = index % 2 == 0
        condition2 = x % 2 == 1
        if condition1 and condition2:
            result += x
        index += 1
    return result