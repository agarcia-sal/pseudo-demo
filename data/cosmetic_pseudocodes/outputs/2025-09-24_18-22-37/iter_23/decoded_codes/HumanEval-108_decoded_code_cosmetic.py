from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        negation_flag = 1
        if integer_value < 0:
            integer_value = -integer_value
            negation_flag = -1

        digits_string = str(integer_value)
        digits_list: List[int] = []
        index = 0
        while index < len(digits_string):
            digits_list.append(int(digits_string[index]))
            index += 1

        first_digit = digits_list[0]
        digits_list[0] = first_digit * negation_flag

        total_sum = 0
        k = 0
        while k < len(digits_list):
            total_sum += digits_list[k]
            k += 1
        return total_sum

    computed_sums: List[int] = []
    i = 0
    while i < len(array_of_integers):
        value = array_of_integers[i]
        sum_val = digits_sum(value)
        computed_sums.append(sum_val)
        i += 1

    positive_sums: List[int] = []
    j = 0
    while j < len(computed_sums):
        current_element = computed_sums[j]
        if current_element > 0:
            positive_sums.append(current_element)
        j += 1

    return len(positive_sums)