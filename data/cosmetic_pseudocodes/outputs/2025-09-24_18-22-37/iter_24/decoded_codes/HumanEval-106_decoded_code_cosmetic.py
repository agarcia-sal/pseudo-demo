from typing import List

def f(integer_n: int) -> List[int]:
    accumulated_results: List[int] = []
    outer_index: int = 1
    while outer_index <= integer_n:
        if outer_index % 2 != 0:
            temp_sum: int = 0
            inner_counter: int = 1
            while inner_counter <= outer_index:
                temp_sum += inner_counter
                inner_counter += 1
            value_to_append = temp_sum
        else:
            temp_product: int = 1
            inner_counter = 1
            while inner_counter <= outer_index:
                temp_product *= inner_counter
                inner_counter += 1
            value_to_append = temp_product
        accumulated_results.append(value_to_append)
        outer_index += 1
    return accumulated_results