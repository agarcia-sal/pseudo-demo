def solution(lst):
    sum_result = 0
    index = 0
    while index < len(lst):
        element = lst[index]
        if index % 2 == 0 and element % 2 == 1:
            sum_result += element
        index += 1
    return sum_result