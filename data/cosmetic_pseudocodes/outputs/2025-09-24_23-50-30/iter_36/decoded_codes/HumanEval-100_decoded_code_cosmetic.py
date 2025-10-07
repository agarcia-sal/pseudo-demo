from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    def generate_sequence(current_index: int, collected_elements: List[int]) -> List[int]:
        if current_index == positive_integer_n:
            return collected_elements
        else:
            # Append positive_integer_n + 2 * current_index to the collected_elements and recurse
            return generate_sequence(current_index + 1, collected_elements + [positive_integer_n + 2 * current_index])
    return generate_sequence(0, [])