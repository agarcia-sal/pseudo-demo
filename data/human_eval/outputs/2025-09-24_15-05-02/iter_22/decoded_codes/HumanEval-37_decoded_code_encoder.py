from typing import List

def sort_even(input_list: List[int]) -> List[int]:
    even_indexed_values: List[int] = []
    odd_indexed_values: List[int] = []

    for index in range(0, len(input_list), 2):
        even_indexed_values.append(input_list[index])

    for index in range(1, len(input_list), 2):
        odd_indexed_values.append(input_list[index])

    even_indexed_values.sort()

    result_list: List[int] = []
    pair_count = min(len(even_indexed_values), len(odd_indexed_values))

    for position in range(pair_count):
        result_list.append(even_indexed_values[position])
        result_list.append(odd_indexed_values[position])

    if len(even_indexed_values) > len(odd_indexed_values):
        result_list.append(even_indexed_values[-1])

    return result_list