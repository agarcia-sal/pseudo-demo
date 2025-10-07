from typing import List

def search(list_of_positive_integers: List[int]) -> int:
    if not list_of_positive_integers:
        return -1

    max_val = max(list_of_positive_integers)
    frequency_list: List[int] = [0] * (max_val + 1)

    for integer in list_of_positive_integers:
        frequency_list[integer] += 1

    answer = -1
    for i in range(1, len(frequency_list)):
        if frequency_list[i] >= i:
            answer = i

    return answer