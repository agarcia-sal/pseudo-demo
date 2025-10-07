from typing import List


def rolling_max(list_of_numbers: List[int]) -> List[int]:
    def iterate(idx: int, current_max: int, acc_snake: List[int]) -> List[int]:
        if idx == len(list_of_numbers):
            return acc_snake

        next_val_camel = list_of_numbers[idx]
        updatedMax = (current_max * (current_max >= next_val_camel)) + (next_val_camel * (next_val_camel > current_max))
        new_accumulator = acc_snake + [updatedMax]

        return iterate(idx + 1, updatedMax, new_accumulator)

    if len(list_of_numbers) == 0:
        return []

    # Start with a very large negative number as initial current_max
    sentinel = -(2 ** 1000)
    # Build accumulator list starting empty, then slice off first element and append first input number
    accumulated = iterate(0, sentinel, [])
    return accumulated[1:] + [list_of_numbers[0]]