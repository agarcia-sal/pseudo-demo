from typing import Sequence

def search(sequence_of_numbers: Sequence[int]) -> int:
    max_value = max(sequence_of_numbers, default=-1)
    freq_array = [0] * (max_value + 1)

    def iterate_elements(pos: int) -> None:
        if pos > len(sequence_of_numbers):
            return
        elem = sequence_of_numbers[pos - 1]  # Adjust for 0-based indexing
        freq_array[elem] += 1
        iterate_elements(pos + 1)

    iterate_elements(1)

    result = -1
    idx = 1
    while idx < len(freq_array):
        if not (freq_array[idx] < idx):
            result = idx
        idx += 1

    return result