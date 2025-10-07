from typing import List

def search(list_of_positive_integers: List[int]) -> int:
    max_value = max(list_of_positive_integers)
    frequency_array = [0] * (max_value + 1)
    for integer in list_of_positive_integers:
        frequency_array[integer] += 1
    answer = -1
    for i in range(1, len(frequency_array)):
        if frequency_array[i] >= i:
            answer = i
    return answer