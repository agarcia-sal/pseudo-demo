from typing import Iterable, List


def sort_array(input_sequence: Iterable[int]) -> List[int]:
    def count_ones_in_binary(number: int) -> int:
        count_ones: int = 0
        temp_num: int = number
        while temp_num > 0:
            if temp_num % 2 == 1:
                count_ones += 1
            temp_num //= 2
        return count_ones

    temp_sorted_sequence: List[int] = [item for item in input_sequence]

    n: int = len(temp_sorted_sequence)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if temp_sorted_sequence[j] > temp_sorted_sequence[j + 1]:
                temp_sorted_sequence[j], temp_sorted_sequence[j + 1] = temp_sorted_sequence[j + 1], temp_sorted_sequence[j]

    index_tracker: int = 0
    while index_tracker < n:
        key_value: int = count_ones_in_binary(temp_sorted_sequence[index_tracker])
        inner_index: int = index_tracker + 1
        while inner_index < n:
            current_value_ones = count_ones_in_binary(temp_sorted_sequence[inner_index])
            if current_value_ones < key_value:
                temp_sorted_sequence[index_tracker], temp_sorted_sequence[inner_index] = (
                    temp_sorted_sequence[inner_index],
                    temp_sorted_sequence[index_tracker],
                )
                key_value = count_ones_in_binary(temp_sorted_sequence[index_tracker])
            inner_index += 1
        index_tracker += 1

    return temp_sorted_sequence