from typing import List

def get_odd_collatz(positive_integer: int) -> List[int]:
    if positive_integer <= 0:
        raise ValueError("Input must be a positive integer")
    if positive_integer % 2 == 0:
        odd_numbers_in_collatz: List[int] = []
    else:
        odd_numbers_in_collatz = [positive_integer]

    while positive_integer > 1:
        if positive_integer % 2 == 0:
            positive_integer //= 2
        else:
            positive_integer = positive_integer * 3 + 1

        if positive_integer % 2 == 1:
            odd_numbers_in_collatz.append(positive_integer)

    return sorted(odd_numbers_in_collatz)