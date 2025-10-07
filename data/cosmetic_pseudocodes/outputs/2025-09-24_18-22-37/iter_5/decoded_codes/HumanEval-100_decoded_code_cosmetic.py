from typing import List

def make_a_pile(number_positive: int) -> List[int]:
    result_collection: List[int] = []
    current_index: int = 0
    while current_index < number_positive:
        computed_value: int = number_positive
        increment_part: int = current_index * 2
        value_to_append: int = computed_value + increment_part
        result_collection.append(value_to_append)
        current_index += 1
    return result_collection