from typing import List

def f(integer_n: int) -> List[int]:
    result_list: List[int] = []
    for integer_i in range(1, integer_n + 1):
        if integer_i % 2 == 0:
            # factorial for even integer_i
            factorial_value = 1
            for integer_j in range(1, integer_i + 1):
                factorial_value *= integer_j
            result_list.append(factorial_value)
        else:
            # sum for odd integer_i
            sum_value = 0
            for integer_j in range(1, integer_i + 1):
                sum_value += integer_j
            result_list.append(sum_value)
    return result_list