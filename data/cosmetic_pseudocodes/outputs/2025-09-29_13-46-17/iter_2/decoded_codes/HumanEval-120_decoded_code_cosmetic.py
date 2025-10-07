from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    def helper(index: int, result_list: List[int]) -> List[int]:
        if index < 0:
            return result_list
        else:
            return helper(index - 1, [array_of_integers[index]] + result_list)

    if positive_integer_k <= 0:
        return []

    sorted_arr = sorted(array_of_integers)
    # helper operates on original array_of_integers, which matches the pseudocode,
    # so using array_of_integers as is, then slicing after helper.
    # But sorted_arr is unused in helper per pseudocode.
    # The pseudocode assigns sorted_arr then calls helper on array_of_integers,
    # but returns helper(...)[-positive_integer_k..]
    # The pseudocode's sequence is ambiguous because helper is called on index over sorted_arr length,
    # but content added to result_list is from array_of_integers[index].
    # To be faithful to pseudocode:
    # - sorted_arr assigned and sorted, but helper always appends array_of_integers[index]
    # - step index from len(sorted_arr) -1 down to 0. This preserves length.
    # So final result length is len(sorted_arr).
    # Then return last positive_integer_k elements.

    # To replicate pseudocode, assign sorted_arr, but helper uses array_of_integers elements, indexing by index.
    # Inconsistent data, but faithfully replicate.
    return helper(len(sorted_arr) - 1, [])[ -positive_integer_k :]