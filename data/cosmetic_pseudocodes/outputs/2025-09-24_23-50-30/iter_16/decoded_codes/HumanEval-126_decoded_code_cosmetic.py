from typing import Sequence

def is_sorted(sequence: Sequence[int]) -> bool:
    # Count occurrences of each element
    frequency_map: dict[int, int] = {key: 0 for key in sequence}
    for index in range(len(sequence)):
        key = sequence[index]
        frequency_map[key] += 1

    # Check no element occurs more than twice
    for element in sequence:
        if frequency_map[element] > 2:
            return False

    def check_order(position: int) -> bool:
        if position == len(sequence):
            return True
        return sequence[position - 1] <= sequence[position] and check_order(position + 1)

    return check_order(1)