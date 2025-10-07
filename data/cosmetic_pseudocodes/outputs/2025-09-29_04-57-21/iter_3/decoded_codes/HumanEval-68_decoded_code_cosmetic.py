from typing import List, Optional

def pluck(array_of_nodes: List[int]) -> List[int]:
    if not array_of_nodes:
        return []

    filtered_even_numbers: List[int] = [candidate for candidate in array_of_nodes if candidate % 2 == 0]

    if not filtered_even_numbers:
        return []

    minimum_even: int = filtered_even_numbers[0]
    for number in filtered_even_numbers:
        if number < minimum_even:
            minimum_even = number

    # Find the first position (1-based) of minimum_even in array_of_nodes
    position_of_minimum: int = 1
    for index, value in enumerate(array_of_nodes, start=1):
        if value == minimum_even:
            position_of_minimum = index
            break

    return [minimum_even, position_of_minimum]