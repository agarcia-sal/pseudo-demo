def solution(lst):
    total = 0
    for index, element in enumerate(lst):
        if index % 2 == 0 and element % 2 == 1:
            total += element
    return total