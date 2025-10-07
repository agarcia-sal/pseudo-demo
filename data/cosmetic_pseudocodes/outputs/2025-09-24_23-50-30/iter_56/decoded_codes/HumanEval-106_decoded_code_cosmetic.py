from typing import List

def f(parameter_p: int) -> List[int]:
    result_array: List[int] = []
    index_counter: int = 1

    while index_counter <= parameter_p:
        if index_counter % 2 == 0:
            intermediate_product: int = 1
            iterator_k: int = 1
            while iterator_k <= index_counter:
                intermediate_product *= iterator_k
                iterator_k += 1
            accumulator_var: int = intermediate_product
        else:
            intermediate_sum: int = 0
            iterator_m: int = 1
            while iterator_m <= index_counter:
                intermediate_sum += iterator_m
                iterator_m += 1
            accumulator_var = intermediate_sum

        result_array.append(accumulator_var)
        index_counter += 1

    return result_array