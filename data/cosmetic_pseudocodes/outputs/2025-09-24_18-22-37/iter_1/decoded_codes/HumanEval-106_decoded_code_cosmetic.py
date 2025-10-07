from typing import List

def f(integer_n: int) -> List[int]:
    result_list: List[int] = []
    for integer_i in range(1, integer_n + 1):
        if integer_i % 2 == 0:
            factorial_value = 1
            counter = 1
            while counter <= integer_i:
                factorial_value *= counter
                counter += 1
            result_list.append(factorial_value)
        else:
            summation_value = 0
            counter = 1
            while counter <= integer_i:
                summation_value += counter
                counter += 1
            result_list.append(summation_value)
    return result_list