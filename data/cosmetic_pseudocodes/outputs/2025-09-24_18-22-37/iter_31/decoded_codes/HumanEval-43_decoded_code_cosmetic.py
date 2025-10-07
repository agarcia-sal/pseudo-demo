from typing import Sequence


def pairs_sum_to_zero(array_of_numbers: Sequence[int]) -> bool:
    total_length: int = len(array_of_numbers)
    peak_index: int = total_length - 1
    position_a: int = 0
    has_zero_pair: bool = False

    while position_a < peak_index and not has_zero_pair:
        value_a: int = array_of_numbers[position_a]
        position_b: int = position_a + 1

        while position_b <= peak_index and not has_zero_pair:
            value_b: int = array_of_numbers[position_b]
            combined_sum: int = value_a + value_b

            if combined_sum == 0:
                has_zero_pair = True
            position_b += 1

        position_a += 1

    return has_zero_pair