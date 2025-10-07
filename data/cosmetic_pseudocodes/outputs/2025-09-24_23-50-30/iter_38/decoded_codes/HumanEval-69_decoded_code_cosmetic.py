from typing import List

def search(array_of_nums: List[int]) -> int:
    if not array_of_nums:
        return -1
    max_val = max(array_of_nums)
    freq_array = [0] * (max_val + 1)
    for element in array_of_nums:
        freq_array[element] += 1
    result = -1
    for counter in range(1, len(freq_array)):
        if freq_array[counter] >= counter:
            result = counter
    return result