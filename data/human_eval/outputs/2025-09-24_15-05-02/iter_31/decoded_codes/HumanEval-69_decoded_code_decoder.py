from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1
    max_val = max(list_of_integers)
    if max_val < 1:
        return -1
    frequency_list = [0] * (max_val + 1)
    for integer in list_of_integers:
        if 0 <= integer <= max_val:
            frequency_list[integer] += 1
    answer = -1
    for index in range(1, len(frequency_list)):
        if frequency_list[index] >= index:
            answer = index
    return answer