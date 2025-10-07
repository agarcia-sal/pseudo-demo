from typing import List

def f(integer_n: int) -> List[int]:
    result_list: List[int] = []
    for index in range(1, integer_n + 1):
        if index % 2 == 0:
            factorial_value = 1
            for multiplier in range(1, index + 1):
                factorial_value *= multiplier
            result_list.append(factorial_value)
        else:
            sum_value = 0
            for addend in range(1, index + 1):
                sum_value += addend
            result_list.append(sum_value)
    return result_list