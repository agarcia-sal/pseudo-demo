from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    temp_sorted_array = array_of_integers[:]  # copy to avoid mutating input
    index = 0
    length = len(temp_sorted_array)
    while index < length - 1:
        position = 0
        while position < length - 1 - index:
            if temp_sorted_array[position] > temp_sorted_array[position + 1]:
                holder = temp_sorted_array[position]
                temp_sorted_array[position] = temp_sorted_array[position + 1]
                temp_sorted_array[position + 1] = holder
            position += 1
        index += 1

    def count_ones_in_binary(number: int) -> int:
        if number == 0:
            return 0
        binary_string = ''
        temp_number = number
        while temp_number > 0:
            digit = temp_number % 2
            binary_string += str(digit)
            temp_number //= 2

        ones_counter = 0
        iterator = 0
        length_bin = len(binary_string)
        while iterator < length_bin:
            if binary_string[iterator] == '1':
                ones_counter += 1
            iterator += 1
        return ones_counter

    i = 0
    while i < length - 1:
        j = 0
        while j < length - 1 - i:
            if count_ones_in_binary(temp_sorted_array[j]) > count_ones_in_binary(temp_sorted_array[j + 1]):
                swapper = temp_sorted_array[j]
                temp_sorted_array[j] = temp_sorted_array[j + 1]
                temp_sorted_array[j + 1] = swapper
            j += 1
        i += 1

    return temp_sorted_array