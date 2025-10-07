from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    results_collection: List[int] = []
    current_counter: int = 0

    while current_counter < positive_integer_n:
        computed_element: int = positive_integer_n + (current_counter * 2)
        results_collection.append(computed_element)
        current_counter += 1

    return results_collection