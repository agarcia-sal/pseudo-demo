from typing import List, Tuple


def pluck(collection_of_items: List[int]) -> List[int]:
    def seek_even(items: List[int], position: int, accumulator: List[int]) -> List[int]:
        if position >= len(items):
            return accumulator
        if items[position] % 2 == 0:
            accumulator.append(items[position])
        return seek_even(items, position + 1, accumulator)

    def find_minimum(numbers: List[int], current_index: int, min_val: int, min_pos: int) -> Tuple[int, int]:
        if current_index >= len(numbers):
            return min_val, min_pos
        if numbers[current_index] < min_val:
            return find_minimum(numbers, current_index + 1, numbers[current_index], current_index)
        return find_minimum(numbers, current_index + 1, min_val, min_pos)

    filtered_evens = seek_even(collection_of_items, 0, [])
    if not filtered_evens:
        return []

    min_even, min_index = find_minimum(filtered_evens, 0, filtered_evens[0], 0)

    def lookup_index(items: List[int], target: int, index: int) -> int:
        if index >= len(items):
            return -1
        if items[index] == target:
            return index
        return lookup_index(items, target, index + 1)

    original_index = lookup_index(collection_of_items, min_even, 0)

    return [min_even, original_index]