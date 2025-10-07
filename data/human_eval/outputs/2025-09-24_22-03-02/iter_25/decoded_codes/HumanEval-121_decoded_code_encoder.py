def solution(lst):
    result = 0
    length = len(lst)
    index = 0
    while index < length:
        x = lst[index]
        if index % 2 == 0 and x % 2 == 1:
            result += x
        index += 1
    return result