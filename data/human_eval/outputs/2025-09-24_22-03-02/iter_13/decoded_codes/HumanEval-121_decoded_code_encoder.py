def solution(lst):
    result_list = [x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1]
    total_sum = sum(result_list)
    return total_sum