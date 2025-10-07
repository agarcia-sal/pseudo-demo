from typing import List


def sort_non_descending(collection: List[int]) -> None:
    n = len(collection)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]


def sort_even(list_input: List[int]) -> List[int]:
    def recursive_zip(accumulator: List[int], list_a: List[int], list_b: List[int], index: int) -> List[int]:
        if index >= len(list_b):
            return accumulator
        concat_elements = [list_a[index], list_b[index]]
        accumulator.extend(concat_elements)
        return recursive_zip(accumulator, list_a, list_b, index + 1)

    temp_even: List[int] = []
    temp_odd: List[int] = []
    for position in range(len(list_input)):
        if position % 2 == 0:
            temp_even.append(list_input[position])
        else:
            temp_odd.append(list_input[position])

    sort_non_descending(temp_even)

    result_sequence: List[int] = recursive_zip([], temp_even, temp_odd, 0)

    if len(temp_even) > len(temp_odd):
        result_sequence.append(temp_even[-1])

    return result_sequence