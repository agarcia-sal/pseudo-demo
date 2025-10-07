def solution(lst):
    total = 0
    for index in range(len(lst) - 1):
        element = lst[index]
        if index % 2 == 0 and element % 2 == 1:
            total += element
    return total