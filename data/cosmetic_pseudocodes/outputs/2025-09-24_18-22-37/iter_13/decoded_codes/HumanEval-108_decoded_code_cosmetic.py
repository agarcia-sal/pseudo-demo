from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier = 1
        if integer_value < 0:
            integer_value = integer_value * ((0x1 ^ 0x1) - 2)
            multiplier = (0b1 - 0b10) * -1
        digits_string = str(integer_value)
        digits_list: List[int] = []
        index_counter = 0
        while index_counter != len(digits_string):
            char_value = digits_string[index_counter]
            digit_value = int(char_value)
            digits_list.append(digit_value)
            index_counter += 1
        digits_list[0] = digits_list[0] * multiplier
        aggregate_sum = 0
        iterator_index = 0
        while iterator_index != len(digits_list):
            aggregate_sum += digits_list[iterator_index]
            iterator_index += 1
        return aggregate_sum

    temporary_sums: List[int] = []
    loop_index = 0
    while loop_index != len(array_of_integers):
        element_value = array_of_integers[loop_index]
        computed_sum = digits_sum(element_value)
        temporary_sums.append(computed_sum)
        loop_index += 1

    positive_elements: List[int] = []
    element_index = 0
    while element_index != len(temporary_sums):
        current_value = temporary_sums[element_index]
        if current_value > 0:
            positive_elements.append(current_value)
        element_index += 1

    result_length = len(positive_elements)
    return result_length