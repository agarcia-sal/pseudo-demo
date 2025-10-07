from typing import List, Callable

def sort_array(numbers: List[int]) -> List[int]:
    def count_ones(bitstring: str, index: int, tally: int) -> int:
        if index == len(bitstring):
            return tally
        return count_ones(bitstring, index + 1, tally + (1 if bitstring[index] == '1' else 0))

    preliminary_step: List[int] = sorted(numbers)

    def ones_key(element: int) -> int:
        binary_version = bin(element)[2:]
        return count_ones(binary_version, 0, 0)

    comparator = Callable[[int, int], int]

    def stable_sort(list_to_sort: List[int], comparator: comparator) -> List[int]:
        if len(list_to_sort) <= 1:
            return list_to_sort
        pivot_index = len(list_to_sort) // 2
        pivot_element = list_to_sort[pivot_index]
        lesser: List[int] = []
        equal: List[int] = []
        greater: List[int] = []

        for candidate in list_to_sort:
            comp_result = comparator(candidate, pivot_element)
            if comp_result < 0:
                lesser.append(candidate)
            elif comp_result == 0:
                equal.append(candidate)
            else:
                greater.append(candidate)
        return stable_sort(lesser, comparator) + equal + stable_sort(greater, comparator)

    def compare_by_ones(a: int, b: int) -> int:
        a_key = ones_key(a)
        b_key = ones_key(b)
        if a_key < b_key:
            return -1
        if a_key > b_key:
            return 1
        return 0

    return stable_sort(preliminary_step, compare_by_ones)