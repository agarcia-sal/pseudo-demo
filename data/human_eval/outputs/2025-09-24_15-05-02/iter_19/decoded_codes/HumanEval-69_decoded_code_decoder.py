from typing import List

def search(list_of_positive_integers: List[int]) -> int:
    max_value: int = max(list_of_positive_integers)
    frequency_list: List[int] = [0] * (max_value + 1)
    for integer in list_of_positive_integers:
        frequency_list[integer] += 1
    answer: int = -1
    for integer in range(1, len(frequency_list)):
        if frequency_list[integer] >= integer:
            answer = integer
    return answer