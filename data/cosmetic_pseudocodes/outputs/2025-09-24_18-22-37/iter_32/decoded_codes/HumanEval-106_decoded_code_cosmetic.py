from typing import List

def f(integer_n: int) -> List[int]:
    result_accumulator: List[int] = []
    counter: int = 1
    while counter <= integer_n:
        parity_check = counter % 2
        if parity_check != 1:
            product_accum: int = 1
            iterator_var: int = 1
            while iterator_var <= counter:
                product_accum *= iterator_var
                iterator_var += 1
            result_accumulator.append(product_accum)
        else:
            sum_accum: int = 0
            step_var: int = 1
            while step_var <= counter:
                sum_accum += step_var
                step_var += 1
            result_accumulator.append(sum_accum)
        counter += 1
    return result_accumulator