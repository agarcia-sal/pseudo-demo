def solution(lst):
    total_sum = 0
    index = 0
    while index < len(lst):
        x = lst[index]
        if index % 2 == 0 and x % 2 == 1:
            total_sum += x
        index += 1
    return total_sum