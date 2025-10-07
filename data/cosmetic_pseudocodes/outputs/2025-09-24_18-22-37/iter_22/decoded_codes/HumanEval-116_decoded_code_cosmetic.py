from typing import List

def sort_array(sequence_of_numbers: List[int]) -> List[int]:
    interim_list: List[int] = sequence_of_numbers
    interim_sorted: List[int] = []
    index_counter: int = 0
    while index_counter < len(interim_list):
        interim_sorted.append(interim_list[index_counter])
        index_counter += 1

    ascending_sorted: List[int] = interim_sorted
    current_position: int = 0
    # Selection sort in ascending order
    while current_position < len(ascending_sorted) - 1:
        smallest_position: int = current_position
        find_position: int = current_position + 1
        while find_position < len(ascending_sorted):
            if ascending_sorted[find_position] < ascending_sorted[smallest_position]:
                smallest_position = find_position
            find_position += 1
        if smallest_position != current_position:
            ascending_sorted[current_position], ascending_sorted[smallest_position] = (
                ascending_sorted[smallest_position],
                ascending_sorted[current_position],
            )
        current_position += 1

    def count_ones_in_binary(value: int) -> int:
        bits: List[int] = []
        temp_value = value
        while True:
            bits.insert(0, temp_value % 2)
            temp_value //= 2
            if temp_value == 0:
                break
        ones_count: int = 0
        i: int = 0
        while i < len(bits):
            if bits[i] == 1:
                ones_count += 1
            i += 1
        return ones_count

    idx_to_process: int = 0
    while idx_to_process < len(ascending_sorted):
        j: int = idx_to_process + 1
        while j < len(ascending_sorted):
            count_j = count_ones_in_binary(ascending_sorted[j])
            count_idx = count_ones_in_binary(ascending_sorted[idx_to_process])
            if count_j < count_idx:
                ascending_sorted[idx_to_process], ascending_sorted[j] = (
                    ascending_sorted[j],
                    ascending_sorted[idx_to_process],
                )
            elif count_j == count_idx:
                if ascending_sorted[j] < ascending_sorted[idx_to_process]:
                    ascending_sorted[idx_to_process], ascending_sorted[j] = (
                        ascending_sorted[j],
                        ascending_sorted[idx_to_process],
                    )
            j += 1
        idx_to_process += 1

    return ascending_sorted