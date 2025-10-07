from typing import Sequence

def minSubArraySum(arbitrary_numbers: Sequence[int]) -> int:
    accumulator: int = 0
    best_so_far: int = 0
    iterator_index: int = 0
    length: int = len(arbitrary_numbers)

    while iterator_index < length:
        current_element: int = arbitrary_numbers[iterator_index]
        accumulator += -current_element  # accumulate negated values
        if accumulator < 0:
            accumulator = 0
        if accumulator > best_so_far:
            best_so_far = accumulator
        iterator_index += 1

    if best_so_far == 0:
        provisional_values = [-arbitrary_numbers[i] for i in range(length)]
        best_so_far = provisional_values[0]
        scan_pos = 1
        while scan_pos < length:
            if provisional_values[scan_pos] > best_so_far:
                best_so_far = provisional_values[scan_pos]
            scan_pos += 1

    result: int = -best_so_far
    return result