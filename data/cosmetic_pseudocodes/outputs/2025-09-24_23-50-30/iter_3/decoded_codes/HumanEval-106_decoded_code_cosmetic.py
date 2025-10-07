from typing import List


def f(integer_n: int) -> List[int]:
    output_array: List[int] = []
    integer_k: int = 1
    while integer_k <= integer_n:
        if integer_k % 2 == 0:
            product_accumulator: int = 1
            integer_m: int = 1
            while integer_m <= integer_k:
                product_accumulator *= integer_m
                integer_m += 1
            output_array.append(product_accumulator)
        else:
            total_sum: int = 0
            integer_m: int = 1
            while integer_m <= integer_k:
                total_sum += integer_m
                integer_m += 1
            output_array.append(total_sum)
        integer_k += 1
    return output_array