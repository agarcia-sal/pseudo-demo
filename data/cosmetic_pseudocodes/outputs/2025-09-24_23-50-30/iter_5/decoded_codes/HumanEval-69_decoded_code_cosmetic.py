from typing import Sequence

def search(input_sequence: Sequence[int]) -> int:
    if not input_sequence:
        return -1  # Handle empty input gracefully

    max_elem = max(input_sequence)
    counts = [0] * (max_elem + 1)

    for element in input_sequence:
        counts[element] += 1

    def recursive_check(pos: int, current_result: int) -> int:
        if pos < 1:
            return current_result
        updated_result = pos if counts[pos] >= pos else current_result
        return recursive_check(pos - 1, updated_result)

    return recursive_check(len(counts) - 1, -1)