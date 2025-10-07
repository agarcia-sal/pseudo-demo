from typing import List

def f(param_x: int) -> List[int]:
    accumulator: List[int] = []
    index_counter: int = 1

    while index_counter <= param_x:
        if index_counter % 2 == 0:
            temp_product: int = 1
            iter_var: int = 1
            while iter_var <= index_counter:
                temp_product *= iter_var
                iter_var += 1
            value_to_add = temp_product
        else:
            temp_sum: int = 0
            iter_var2: int = 1
            while iter_var2 <= index_counter:
                temp_sum += iter_var2
                iter_var2 += 1
            value_to_add = temp_sum

        accumulator.append(value_to_add)
        index_counter += 1

    return accumulator