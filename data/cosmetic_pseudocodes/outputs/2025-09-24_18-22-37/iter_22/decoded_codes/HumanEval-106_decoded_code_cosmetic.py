from typing import List


def f(count: int) -> List[int]:
    accumulation: List[int] = []
    outer_counter: int = 1
    while outer_counter <= count:
        is_even: bool = (outer_counter % 2) == 0
        if not is_even:
            sum_accumulator: int = 0
            inner_index: int = 1
            # Repeat adding inner_index until inner_index > outer_counter
            while inner_index <= outer_counter:
                sum_accumulator += inner_index
                inner_index += 1
            value_to_add: int = sum_accumulator
        else:
            fact_accumulator: int = 1
            inner_index: int = 1
            while inner_index <= outer_counter:
                fact_accumulator *= inner_index
                inner_index += 1
            value_to_add = fact_accumulator
        accumulation.append(value_to_add)
        outer_counter += 1
    return accumulation