from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_input: int) -> int:
        multiplier_sign: int = 1
        if integer_input < 0:
            integer_input = -integer_input
            multiplier_sign = -multiplier_sign

        digit_chars: List[str] = list(str(integer_input))
        digit_values: List[int] = []
        idx: int = 0
        while idx < len(digit_chars):
            digit_values.append(int(digit_chars[idx]))
            idx += 1

        digit_values[0] *= multiplier_sign

        total_sum: int = 0
        pos: int = 0
        while pos < len(digit_values):
            total_sum += digit_values[pos]
            pos += 1

        return total_sum

    sums_list: List[int] = []
    i: int = 0
    while i != len(array_of_integers):
        current_number = array_of_integers[i]
        current_sum = digits_sum(current_number)
        sums_list = sums_list + [current_sum]
        i += 1

    positive_sums: List[int] = []
    j: int = 0
    while j < len(sums_list):
        if sums_list[j] > 0:
            positive_sums.append(sums_list[j])
        j += 1

    return len(positive_sums)