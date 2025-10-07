from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    accumulator_list: List[int] = []
    current_counter: int = 0
    upper_bound: int = positive_integer_n - 1
    while current_counter <= upper_bound:
        interim_value: int = positive_integer_n
        multiplication_result: int = 2 * current_counter
        interim_value += multiplication_result
        accumulator_list.append(interim_value)
        current_counter += 1
    return accumulator_list