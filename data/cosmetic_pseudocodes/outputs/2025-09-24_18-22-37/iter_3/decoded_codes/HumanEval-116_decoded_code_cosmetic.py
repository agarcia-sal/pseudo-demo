from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    def TO_BINARY_STRING(num: int) -> str:
        if num == 0:
            return "0b0"
        bin_rep = ""
        n = num
        while n > 0:
            remainder = n % 2
            bin_rep = str(remainder) + bin_rep
            n //= 2
        return "0b" + bin_rep

    def count_ones_in_binary(number: int) -> int:
        binary_str = TO_BINARY_STRING(number)
        ones_count = 0
        # The binary string starts with '0b', count from index 2 onwards
        for char_index in range(2, len(binary_str)):
            if binary_str[char_index] == '1':
                ones_count += 1
        return ones_count

    def insertion_sort_ascending(lst: List[int]) -> List[int]:
        for i in range(1, len(lst)):
            key = lst[i]
            j = i - 1
            while j >= 0 and lst[j] > key:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key
        return lst

    def sort_by_binary_ones(input_list: List[int], index: int) -> List[int]:
        if index == len(input_list):
            return input_list
        current = input_list[index]
        pos = index
        while pos > 0 and count_ones_in_binary(input_list[pos - 1]) > count_ones_in_binary(current):
            input_list[pos] = input_list[pos - 1]
            pos -= 1
        input_list[pos] = current
        return sort_by_binary_ones(input_list, index + 1)

    decimal_sorted = insertion_sort_ascending(array_of_integers)
    sort_by_binary_ones(decimal_sorted, 1)
    return decimal_sorted