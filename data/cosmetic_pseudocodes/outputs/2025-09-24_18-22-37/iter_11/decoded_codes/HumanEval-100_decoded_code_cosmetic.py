from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result_collection: List[int] = []
    iteration_counter: int = 0
    max_index: int = positive_integer_n - 1

    while iteration_counter <= max_index:
        temp_multiplier: int = 2
        temp_product: int = temp_multiplier * iteration_counter
        temp_value: int = positive_integer_n + temp_product
        result_collection.append(temp_value)

        iteration_counter += 1

    return result_collection