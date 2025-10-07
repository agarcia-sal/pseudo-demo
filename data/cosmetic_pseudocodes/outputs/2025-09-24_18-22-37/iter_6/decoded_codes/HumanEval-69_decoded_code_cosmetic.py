from typing import List

def search(sequence_of_numbers: List[int]) -> int:
    if not sequence_of_numbers:
        return -1
    counts_array = [0] * (max(sequence_of_numbers) + 1)
    iterator = 0
    while iterator < len(sequence_of_numbers):
        current_num = sequence_of_numbers[iterator]
        counts_array[current_num] += 1
        iterator += 1
    result = -1
    position = 1
    while position < len(counts_array):
        if counts_array[position] < position:
            position += 1
            continue
        result = position
        position += 1
    return result