from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k != 0:
        def sort_non_decreasing(arr: List[int]) -> None:
            # Insertion sort, stable and straightforward for clarity
            for i in range(1, len(arr)):
                index = i
                while index > 0 and arr[index] < arr[index - 1]:
                    arr[index], arr[index - 1] = arr[index - 1], arr[index]
                    index -= 1

        sort_non_decreasing(array_of_integers)

        length_of_arr = len(array_of_integers)
        start_index = length_of_arr - positive_integer_k
        result_accumulator: List[int] = []

        index_loop = start_index
        while index_loop < length_of_arr:
            result_accumulator.append(array_of_integers[index_loop])
            index_loop += 1

        return result_accumulator

    return []