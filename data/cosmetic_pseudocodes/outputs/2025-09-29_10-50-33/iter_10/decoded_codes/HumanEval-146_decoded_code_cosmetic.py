from typing import List


def specialFilter(list_of_numbers: List[int]) -> int:
    tally: int = 0
    idx: int = 0
    while idx < len(list_of_numbers):
        candidate = list_of_numbers[idx]
        if candidate > 10:
            first_digit = int(str(candidate)[0])
            if first_digit in {1, 3, 5, 7, 9}:
                last_digit = int(str(candidate)[-1])
                if last_digit in {1, 3, 5, 7, 9}:
                    tally += 1
        idx += 1
    return tally