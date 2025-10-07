from typing import List, Optional


def pluck(nodes_collection: List[int]) -> List[int]:
    def traverse_filter(current_pos: int, result_set: List[int]) -> List[int]:
        if current_pos == len(nodes_collection):
            return result_set
        current_element = nodes_collection[current_pos]
        updated_set = result_set + [current_element] if current_element % 2 == 0 else result_set
        return traverse_filter(current_pos + 1, updated_set)

    if not nodes_collection:
        return []

    filtered_evens = traverse_filter(0, [])
    if not filtered_evens:
        return []

    candidate_minimum = filtered_evens[0]

    def find_minimum(elements: List[int], idx: int, acc: int) -> int:
        if idx == len(elements):
            return acc
        current = elements[idx]
        if current < acc:
            return find_minimum(elements, idx + 1, current)
        return find_minimum(elements, idx + 1, acc)

    smallest_even_value = find_minimum(filtered_evens, 1, candidate_minimum)

    def locate_value(value: int, collection: List[int], position: int) -> int:
        if position == len(collection):
            return -1
        if collection[position] == value:
            return position
        return locate_value(value, collection, position + 1)

    smallest_even_index = locate_value(smallest_even_value, nodes_collection, 0)

    return [smallest_even_value, smallest_even_index]