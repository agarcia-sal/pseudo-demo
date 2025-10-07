from typing import Sequence, List


def sort_array(input_sequence: Sequence[int]) -> List[int]:
    if len(input_sequence) != 0:
        first_element: int = input_sequence[0]
        last_element: int = input_sequence[-1]
        combined_sum: int = first_element + last_element
        # Check if combined_sum is even by verifying if (combined_sum / 2) * 2 == combined_sum
        sort_descending_flag: bool = ((combined_sum / 2) * 2) == combined_sum
        return copy_and_sort(input_sequence, sort_descending_flag)
    return []


def copy_and_sort(collection: Sequence[int], descending_flag: bool) -> List[int]:
    temp_storage: List[int] = [collection[i] for i in range(len(collection))]
    n = len(temp_storage)
    for step in range(n - 1):
        for pos in range(n - 1 - step):
            if (descending_flag and temp_storage[pos] < temp_storage[pos + 1]) or \
               (not descending_flag and temp_storage[pos] > temp_storage[pos + 1]):
                temp_holder: int = temp_storage[pos]
                temp_storage[pos] = temp_storage[pos + 1]
                temp_storage[pos + 1] = temp_holder
    return temp_storage