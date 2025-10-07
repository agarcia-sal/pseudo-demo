from typing import Sequence, List, Tuple


def sort_array(input_sequence: Sequence[int]) -> List[int]:
    def count_ones(binary_str: str, pos: int, acc: int) -> int:
        if pos < len(binary_str):
            return count_ones(binary_str, pos + 1, acc + 1 if binary_str[pos] == '1' else acc)
        return acc

    # Copy input_sequence to a list (temp_array)
    temp_array: List[int] = []
    idx = 0
    while idx < len(input_sequence):
        temp_array.append(input_sequence[idx])
        idx += 1

    # Bubble sort temp_array by decimal ascending
    n = len(temp_array)
    swapped = True
    while swapped:
        swapped = False
        j = 0
        while j < n - 1:
            if temp_array[j] > temp_array[j + 1]:
                temp_array[j], temp_array[j + 1] = temp_array[j + 1], temp_array[j]
                swapped = True
            j += 1
        n -= 1

    # Pair each element with count of ones in binary representation
    result_array: List[Tuple[int, int]] = []
    for each_element in temp_array:
        bin_str = bin(each_element)
        sum_ones = count_ones(bin_str, 2, 0)  # skip '0b'
        result_array.append((each_element, sum_ones))

    # Bubble sort result_array by count of ones ascending, stable
    k = len(result_array)
    for i in range(k - 1):
        for j in range(k - i - 1):
            if result_array[j][1] > result_array[j + 1][1]:
                result_array[j], result_array[j + 1] = result_array[j + 1], result_array[j]

    # Extract sorted elements
    output_array: List[int] = []
    for pair in result_array:
        output_array.append(pair[0])

    return output_array