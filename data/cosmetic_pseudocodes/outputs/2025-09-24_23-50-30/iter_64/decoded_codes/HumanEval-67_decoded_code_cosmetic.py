from collections import deque
from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def helper_function(queue_representation: deque[str], accumulated_list: List[int]) -> List[int]:
        if not queue_representation:
            return accumulated_list
        current_element = queue_representation.popleft()
        # Check if current_element consists only of digits
        if current_element.isdigit():
            return helper_function(queue_representation, accumulated_list + [int(current_element)])
        else:
            return helper_function(queue_representation, accumulated_list)

    token_list = string_description.split(" ")
    tokens_queue = deque(token_list)
    number_collection = helper_function(tokens_queue, [])

    total_accumulated = sum(number_collection)

    return total_number_of_fruits - total_accumulated