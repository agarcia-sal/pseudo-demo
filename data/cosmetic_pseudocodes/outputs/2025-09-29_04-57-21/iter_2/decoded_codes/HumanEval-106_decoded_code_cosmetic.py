from typing import List

def f(count_limit: int) -> List[int]:
    output_array: List[int] = []
    current_index: int = 1
    while current_index <= count_limit:
        if (current_index & 1) == 0:
            prod_accumulator: int = 1
            step_counter: int = current_index
            while step_counter >= 1:
                prod_accumulator *= step_counter
                step_counter -= 1
            output_array.append(prod_accumulator)
        else:
            sum_accumulator: int = 0
            step_counter: int = 1
            while step_counter <= current_index:
                sum_accumulator += step_counter
                step_counter += 1
            output_array.append(sum_accumulator)
        current_index += 1
    return output_array