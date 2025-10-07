def solution(lst):
    sum_result = 0
    for idx in range(len(lst)):
        if idx % 2 == 0 and lst[idx] % 2 == 1:
            sum_result += lst[idx]
    return sum_result