from typing import List


def count_nums(numbers_array: List[int]) -> int:
    def digits_sum(param_x: int) -> int:
        multiplier_sign = 1
        if param_x < 0:
            param_x = -param_x
            multiplier_sign = -1
        digits_list = str(param_x)
        temp_digits: List[int] = [int(d) for d in digits_list]
        temp_digits[0] *= multiplier_sign
        sum_result = sum(temp_digits)
        return sum_result

    result_list: List[int] = [digits_sum(num) for num in numbers_array]
    positive_elements: List[int] = [val for val in result_list if val > 0]
    final_count = len(positive_elements)
    return final_count