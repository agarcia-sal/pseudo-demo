from functools import reduce
from typing import List


def order_by_points(collection_of_values: List[int]) -> List[int]:
    def inner_digit_sum(value_param: int) -> int:
        direction_flag = 1
        if value_param < 0:
            value_param = -value_param
            direction_flag = -1
        str_value = str(value_param)
        regrouped_indexed_list = [int(ch) for ch in str_value]
        regrouped_indexed_list[0] *= direction_flag
        return reduce(lambda a, b: a + b, regrouped_indexed_list)

    sorted_output = [v for v in collection_of_values]
    sorted_output.sort(key=inner_digit_sum)
    return sorted_output