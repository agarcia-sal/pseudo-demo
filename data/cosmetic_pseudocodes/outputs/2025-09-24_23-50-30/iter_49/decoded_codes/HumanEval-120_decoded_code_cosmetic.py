from typing import List


def sort_non_decreasing(input_array: List[int]) -> None:
    outer_counter: int = 0
    n: int = len(input_array)
    while outer_counter < n - 1:
        inner_counter: int = 0
        while inner_counter < n - outer_counter - 1:
            if input_array[inner_counter] > input_array[inner_counter + 1]:
                input_array[inner_counter], input_array[inner_counter + 1] = (
                    input_array[inner_counter + 1],
                    input_array[inner_counter],
                )
            inner_counter += 1
        outer_counter += 1


def maximum(collection_of_numbers: List[int], count_limit: int) -> List[int]:
    if count_limit == 0:
        return []

    sort_non_decreasing(collection_of_numbers)

    def slice_from_end(data_source: List[int], slice_length: int) -> List[int]:
        if slice_length <= 0:
            return []
        last_index: int = len(data_source) - 1
        return [data_source[last_index]] + slice_from_end(data_source[:last_index], slice_length - 1)

    return slice_from_end(collection_of_numbers, count_limit)