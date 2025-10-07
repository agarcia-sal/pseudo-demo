from typing import Sequence

def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    def helper_scan(position_m: int, current_value: int) -> bool:
        if position_m >= len(sequence_of_numbers):
            return False
        if current_value + sequence_of_numbers[position_m] == 0:
            return True
        return helper_scan(position_m + 1, current_value)

    def main_loop(pointer_n: int) -> bool:
        if pointer_n >= len(sequence_of_numbers) - 1:
            return False
        if helper_scan(pointer_n + 1, sequence_of_numbers[pointer_n]):
            return True
        return main_loop(pointer_n + 1)

    return main_loop(0)