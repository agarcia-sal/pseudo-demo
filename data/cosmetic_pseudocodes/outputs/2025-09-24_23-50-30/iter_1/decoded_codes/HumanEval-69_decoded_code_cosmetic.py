from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1
    max_val = max(list_of_integers)
    frequency_list: List[int] = [0] * (max_val + 1)
    for num in list_of_integers:
        frequency_list[num] += 1
    answer = -1
    limit = len(frequency_list)
    for idx in range(1, limit):
        if frequency_list[idx] >= idx:
            answer = idx
    return answer