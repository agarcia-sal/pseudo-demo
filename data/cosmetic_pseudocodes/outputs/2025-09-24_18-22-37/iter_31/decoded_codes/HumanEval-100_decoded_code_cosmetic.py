from typing import List


def make_a_pile(non_negative_count: int) -> List[int]:
    output_collection: List[int] = []
    step: int = 2
    limit: int = non_negative_count - 1
    current_position: int = 0

    while current_position <= limit:
        element: int = non_negative_count + (step * current_position)
        output_collection.append(element)
        current_position += 1

    return output_collection