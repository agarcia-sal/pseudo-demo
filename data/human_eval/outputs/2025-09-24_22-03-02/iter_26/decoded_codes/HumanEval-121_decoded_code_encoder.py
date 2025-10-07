def solution(lst):
    sum_result = 0
    for idx in range(len(lst)):
        x = lst[idx]
        if idx % 2 == 0 and x % 2 == 1:
            sum_result += x
    return sum_result