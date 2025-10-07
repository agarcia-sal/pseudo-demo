from typing import List


def f(integer_n: int) -> List[int]:
    output_collection: List[int] = []
    counter_outer: int = 1
    while counter_outer <= integer_n:
        current_value: int = counter_outer
        is_even: bool = (current_value % 2) == 0
        if not is_even:
            sum_accumulator: int = 0
            iterator_inner: int = 1
            while iterator_inner <= current_value:
                sum_accumulator += iterator_inner
                iterator_inner += 1
            computed_element: int = sum_accumulator
        else:
            product_accumulator: int = 1
            iterator_inner: int = 1
            while iterator_inner <= current_value:
                product_accumulator *= iterator_inner
                iterator_inner += 1
            computed_element = product_accumulator
        output_collection.append(computed_element)
        counter_outer += 1
    return output_collection