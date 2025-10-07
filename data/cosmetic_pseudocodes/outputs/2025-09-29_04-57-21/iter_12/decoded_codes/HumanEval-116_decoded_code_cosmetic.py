from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    intermediary_sorted: List[int] = array_of_integers.copy()
    temporary_index: int = 0
    n: int = len(intermediary_sorted)

    # Bubble sort the array
    while temporary_index < n - 1:
        cursor: int = 0
        while cursor < n - temporary_index - 1:
            if intermediary_sorted[cursor] > intermediary_sorted[cursor + 1]:
                swap_tmp = intermediary_sorted[cursor]
                intermediary_sorted[cursor] = intermediary_sorted[cursor + 1]
                intermediary_sorted[cursor + 1] = swap_tmp
            cursor += 1
        temporary_index += 1

    def binary_one_digit_count(num: int) -> int:
        binary_form: str = bin(num)[2:]
        count_ones: int = 0
        position: int = 0
        length: int = len(binary_form)
        while position < length:
            if binary_form[position] == '1':
                count_ones += 1
            position += 1
        return count_ones

    final_array: List[int] = []
    scan_index: int = 0
    length_intermediary: int = len(intermediary_sorted)

    while scan_index < length_intermediary:
        current_element: int = intermediary_sorted[scan_index]
        insert_position: int = 0

        while insert_position < len(final_array):
            current_ones = binary_one_digit_count(current_element)
            pos_ones = binary_one_digit_count(final_array[insert_position])
            if current_ones < pos_ones:
                break
            elif current_ones == pos_ones and current_element < final_array[insert_position]:
                break
            insert_position += 1

        final_array.insert(insert_position, current_element)
        scan_index += 1

    return final_array