from typing import List


def count_nums(original_array: List[int]) -> int:
    def digits_sum(aux_num: int) -> int:
        mult_factor: int = 1
        if aux_num < 0:
            aux_num = -aux_num
            mult_factor = -1

        str_repr: str = str(aux_num)
        digit_array: List[int] = [int(ch) for ch in str_repr]
        if digit_array:
            digit_array[0] *= mult_factor

        total: int = sum(digit_array)
        return total

    collected_sums: List[int] = [digits_sum(num) for num in original_array]
    favorable_items: List[int] = [candidate for candidate in collected_sums if candidate > 0]

    result_length: int = len(favorable_items)
    return result_length