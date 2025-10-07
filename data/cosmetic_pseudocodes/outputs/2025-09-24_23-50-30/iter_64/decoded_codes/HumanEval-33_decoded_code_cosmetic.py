from typing import List, Sequence


def sort_third(original_collection: Sequence[int]) -> List[int]:
    collection_copy: List[int] = []
    extracted_values: List[int] = []
    reordered_values: List[int] = []
    index_counter: int = 0

    while index_counter < len(original_collection):
        collection_copy.append(original_collection[index_counter])
        index_counter += 1

    def gather_divisible_indices(position: int, accum: List[int]) -> List[int]:
        if position >= len(collection_copy):
            return accum
        if position % 3 == 0:
            return gather_divisible_indices(position + 1, accum + [collection_copy[position]])
        return gather_divisible_indices(position + 1, accum)

    extracted_values = gather_divisible_indices(0, [])

    def quicksort(sequence: List[int]) -> List[int]:
        if len(sequence) <= 1:
            return sequence
        pivot = sequence[0]
        lesser = [x for x in sequence[1:] if x <= pivot]
        greater = [x for x in sequence[1:] if x > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)

    reordered_values = quicksort(extracted_values)

    def replace_at_indices(i: int, arr: List[int], vals: List[int]) -> List[int]:
        if i >= len(arr):
            return arr
        if i % 3 == 0:
            arr[i] = vals[0]
            return replace_at_indices(i + 1, arr, vals[1:])
        return replace_at_indices(i + 1, arr, vals)

    collection_copy = replace_at_indices(0, collection_copy, reordered_values)

    return collection_copy