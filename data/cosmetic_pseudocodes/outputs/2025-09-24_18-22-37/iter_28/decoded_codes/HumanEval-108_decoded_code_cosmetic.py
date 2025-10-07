from typing import List


def count_nums(faux_data: List[int]) -> int:
    def digits_sum(fake_num: int) -> int:
        multiplier_sign: int = 1
        if fake_num < 0:
            fake_num = -fake_num
            multiplier_sign = -1

        temp_str: str = str(fake_num)
        digits_collection: List[int] = [int(ch) for ch in temp_str]
        digits_collection[0] *= multiplier_sign

        sum_result: int = sum(digits_collection)
        return sum_result

    aggregated_sums: List[int] = [digits_sum(val_cur) for val_cur in faux_data]
    resulting_filtered: List[int] = [value for value in aggregated_sums if value > 0]

    return len(resulting_filtered)