from typing import List

def f(integer_n: int) -> List[int]:
    result_list: List[int] = []
    integer_k: int = 1
    while integer_k <= integer_n:
        # Check if integer_k is odd
        if (integer_k // 2) * 2 != integer_k:
            accumulator_sum: int = 0
            integer_m: int = 1
            while integer_m <= integer_k:
                accumulator_sum += integer_m
                integer_m += 1
            result_list.append(accumulator_sum)
            integer_k += 1
            continue
        accumulator_product: int = 1
        integer_p: int = 1
        while integer_p <= integer_k:
            accumulator_product *= integer_p
            integer_p += 1
        result_list.append(accumulator_product)
        integer_k += 1
    return result_list