from typing import List

def search(list_of_positive_integers: List[int]) -> int:
    max_val = max(list_of_positive_integers, default=0)
    frequency_list: List[int] = [0] * (max_val + 1)
    for integer in list_of_positive_integers:
        frequency_list[integer] += 1
    answer = -1
    for integer_index in range(1, len(frequency_list)):
        if frequency_list[integer_index] >= integer_index:
            answer = integer_index
    return answer