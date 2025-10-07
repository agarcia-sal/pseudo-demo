from typing import List

def count_nums(array_of_integers: List[int]) -> int:

    def digits_sum(integer_value: int) -> int:
        multiplier_flag = 1
        if not (integer_value >= 0):
            integer_value = -integer_value
            multiplier_flag = -1

        digit_chars = str(integer_value)
        digits_list: List[int] = []
        index_counter = 0
        while index_counter < len(digit_chars):
            digits_list.append(int(digit_chars[index_counter]))
            index_counter += 1

        digits_list[0] = digits_list[0] * multiplier_flag

        total_sum = 0
        for digit_element in digits_list:
            total_sum += digit_element

        return total_sum

    sum_collection: List[int] = []
    iterator_index = 0
    while iterator_index < len(array_of_integers):
        sum_collection.append(digits_sum(array_of_integers[iterator_index]))
        iterator_index += 1

    positive_only: List[int] = []
    pos_index = 0
    while pos_index < len(sum_collection):
        if sum_collection[pos_index] > 0:
            positive_only.append(sum_collection[pos_index])
        pos_index += 1

    return len(positive_only)