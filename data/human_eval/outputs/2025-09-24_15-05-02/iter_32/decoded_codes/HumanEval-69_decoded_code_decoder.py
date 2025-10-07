from typing import List

def search(list_of_positive_integers: List[int]) -> int:
    frequency_list: List[int] = [0] * (max(list_of_positive_integers) + 1)
    for integer_value in list_of_positive_integers:
        frequency_list[integer_value] += 1
    answer: int = -1
    for integer_index in range(1, len(frequency_list)):
        if frequency_list[integer_index] >= integer_index:
            answer = integer_index
    return answer