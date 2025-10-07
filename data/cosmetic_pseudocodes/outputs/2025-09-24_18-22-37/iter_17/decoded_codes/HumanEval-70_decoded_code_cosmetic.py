from typing import List

def strange_sort_list(numbers_seq: List[int]) -> List[int]:
    numbers = numbers_seq[:]  # Make a copy to avoid modifying the original list
    output_accumulator: List[int] = []
    pick_minimum: bool = True

    while numbers:
        candidate = numbers[0]
        idx = 0
        for pos in range(1, len(numbers)):
            if pick_minimum:
                if numbers[pos] < candidate:
                    candidate = numbers[pos]
                    idx = pos
            else:
                if numbers[pos] > candidate:
                    candidate = numbers[pos]
                    idx = pos
        output_accumulator.append(candidate)
        numbers.pop(idx)
        pick_minimum = not pick_minimum

    return output_accumulator