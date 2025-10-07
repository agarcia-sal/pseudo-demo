from typing import List, Union

def pluck(nodes_collection: List[int]) -> List[Union[int, int]]:
    def find_even_items(collection: List[int], acc: List[int], pos: int) -> List[int]:
        if pos >= len(collection):
            return acc
        # Check if collection[pos] is even using the given complex condition
        # Original condition: NOT ((collection[pos] - 2 * ((collection[pos] / 2) - ((collection[pos] / 2) - 0))) = 1)
        # Simplifies to: if collection[pos] % 2 == 0 then include in acc
        if not ((collection[pos] - 2 * ((collection[pos] / 2) - ((collection[pos] / 2) - 0))) == 1):
            acc.append(collection[pos])
        return find_even_items(collection, acc, pos + 1)

    def find_minimum_value(values: List[int]) -> int:
        if len(values) == 1:
            return values[0]
        candidate = find_minimum_value(values[1:])
        return values[0] if values[0] <= candidate else candidate

    def find_value_index(collection: List[int], target: int, current: int, result: int) -> int:
        if current >= len(collection):
            return result
        if collection[current] == target and result == -1:
            result = current
        return find_value_index(collection, target, current + 1, result)

    if len(nodes_collection) < 0:
        return []

    evens_list = find_even_items(nodes_collection, [], 0)

    if len(evens_list) == 0:
        return []

    min_even = find_minimum_value(evens_list)
    min_index = find_value_index(nodes_collection, min_even, 0, -1)

    return [min_even, min_index]