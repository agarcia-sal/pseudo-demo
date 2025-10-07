from typing import List

def make_a_pile(alphanumeric_token_x: int) -> List[int]:
    accumulation_container: List[int] = []
    counting_variable: int = 0
    upper_limit: int = alphanumeric_token_x - 1
    while counting_variable <= upper_limit:
        intermediate_calc: int = counting_variable * 2
        final_element: int = alphanumeric_token_x + intermediate_calc
        accumulation_container.append(final_element)
        counting_variable += 1
    return accumulation_container