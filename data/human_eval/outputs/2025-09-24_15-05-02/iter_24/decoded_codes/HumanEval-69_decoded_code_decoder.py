from typing import List

def search(list_of_positive_integers: List[int]) -> int:
    if not list_of_positive_integers:
        return -1  # no valid answer if list is empty
    max_value = max(list_of_positive_integers)
    frequency_array: List[int] = [0] * (max_value + 1)
    for num in list_of_positive_integers:
        frequency_array[num] += 1
    answer = -1
    for index in range(1, max_value + 1):
        if frequency_array[index] >= index:
            answer = index
    return answer