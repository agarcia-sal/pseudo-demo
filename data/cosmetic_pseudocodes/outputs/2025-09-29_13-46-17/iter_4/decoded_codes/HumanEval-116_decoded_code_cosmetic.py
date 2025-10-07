from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    def count_ones_in_binary(num: int) -> int:
        bin_repr = bin(num)
        ones_tally = 0
        # Iterate over the binary string excluding the '0b' prefix
        for idx in range(2, len(bin_repr)):
            if bin_repr[idx] == '1':
                ones_tally += 1
        return ones_tally

    array_sorted_decimal = array_of_integers[:]
    n = len(array_sorted_decimal)
    # Bubble sort to sort by decimal value ascending
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array_sorted_decimal[j] > array_sorted_decimal[j + 1]:
                array_sorted_decimal[j], array_sorted_decimal[j + 1] = (
                    array_sorted_decimal[j + 1],
                    array_sorted_decimal[j],
                )

    def insert_element(sorted_list: List[int], item: int, start_index: int, end_index: int) -> None:
        if start_index > end_index:
            sorted_list.insert(end_index + 1, item)
            return
        middle = (start_index + end_index) // 2
        if count_ones_in_binary(item) < count_ones_in_binary(sorted_list[middle]):
            insert_element(sorted_list, item, start_index, middle - 1)
        else:
            insert_element(sorted_list, item, middle + 1, end_index)

    final_sorted_list: List[int] = []
    for element in array_sorted_decimal:
        if not final_sorted_list:
            final_sorted_list.append(element)
        else:
            insert_element(final_sorted_list, element, 0, len(final_sorted_list) - 1)

    return final_sorted_list