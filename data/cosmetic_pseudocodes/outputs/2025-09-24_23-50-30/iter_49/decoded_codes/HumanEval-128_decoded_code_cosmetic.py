from typing import List, Optional


def prod_sign(array_of_integers: List[int]) -> Optional[int]:
    def compute_sign(accumulator_flag: int, index_position: int) -> int:
        if index_position == len(array_of_integers):
            if accumulator_flag == 0:
                return 0
            return 1 if (accumulator_flag % 2) == 0 else -1
        current_val = array_of_integers[index_position]
        updated_flag = 0 if current_val == 0 else (accumulator_flag + 1 if current_val < 0 else accumulator_flag)
        return compute_sign(updated_flag, index_position + 1)

    if len(array_of_integers) == 0:
        return None

    sign_indicator = compute_sign(0, 0)

    def recursive_sum(position: int, accumulator_sum: int) -> int:
        if position == len(array_of_integers):
            return accumulator_sum
        val = array_of_integers[position]
        return recursive_sum(position + 1, accumulator_sum + (-val if val < 0 else val))

    magnitude_sum = recursive_sum(0, 0)

    return sign_indicator * magnitude_sum