from typing import List, Tuple


def get_max_triples(integer_n: int) -> List[Tuple[int, int, int]]:
    result_triplets: List[Tuple[int, int, int]] = []
    square_calc: List[int] = []

    current_index = 1
    while current_index <= integer_n:
        length = (current_index * current_index) - current_index + 1
        square_calc.append(length)
        current_index += 1

    left_idx = 0
    while left_idx <= integer_n - 1:
        middle_idx = left_idx + 1
        while middle_idx <= integer_n - 1:
            right_idx = middle_idx + 1
            while right_idx <= integer_n - 1:
                if (square_calc[left_idx] + square_calc[middle_idx] + square_calc[right_idx]) % 3 == 0:
                    result_triplets.append(
                        (square_calc[left_idx], square_calc[middle_idx], square_calc[right_idx])
                    )
                right_idx += 1
            middle_idx += 1
        left_idx += 1

    return result_triplets