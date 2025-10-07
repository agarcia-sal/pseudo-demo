from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            sign = -1
        string_digits = str(integer_value)
        digits_list: List[int] = []
        index = 0
        while index < len(string_digits):
            digits_list.append(int(string_digits[index]))
            index += 1
        digits_list[0] *= sign
        total = 0
        i = 0
        while i < len(digits_list):
            total += digits_list[i]
            i += 1
        return total

    result_list: List[int] = []
    pos = 0
    while pos < len(array_of_integers):
        result_list.append(digits_sum(array_of_integers[pos]))
        pos += 1

    positive_results: List[int] = []
    j = 0
    while j < len(result_list):
        if result_list[j] > 0:
            positive_results.append(result_list[j])
        j += 1

    return len(positive_results)