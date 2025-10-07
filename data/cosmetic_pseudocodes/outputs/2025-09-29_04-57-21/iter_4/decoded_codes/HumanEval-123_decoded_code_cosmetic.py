from typing import List


def get_odd_collatz(number: int) -> List[int]:
    sequence: List[int]

    if number % 2 != 0:
        sequence = [number]
    else:
        sequence = []

    while number > 1:
        if number % 2 == 0:
            number = number // 2  # integer division
        else:
            number = 3 * number + 1

        if number % 2 == 1:
            sequence.append(int(number))

    return sorted(sequence)