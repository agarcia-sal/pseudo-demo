from typing import List

def search(array_of_numbers: List[int]) -> int:
    max_element = max(array_of_numbers) if array_of_numbers else 0
    count_array: List[int] = [0] * (max_element + 1)

    for num in array_of_numbers:
        count_array[num] += 1

    result = -1
    for position in range(1, len(count_array)):
        if count_array[position] >= position:
            result = position

    return result