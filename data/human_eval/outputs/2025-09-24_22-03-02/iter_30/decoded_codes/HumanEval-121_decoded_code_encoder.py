def solution(lst):
    sum_result = 0
    n = len(lst)
    i = 0
    while i < n:
        if i % 2 == 0:
            x = lst[i]
            if x % 2 == 1:
                sum_result += x
        i += 1
    return sum_result