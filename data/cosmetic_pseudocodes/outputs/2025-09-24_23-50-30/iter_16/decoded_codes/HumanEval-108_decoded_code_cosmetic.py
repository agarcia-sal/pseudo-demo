from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        if integer_value < 0:
            integer_value = -integer_value
            sign_multiplier = -1
        else:
            sign_multiplier = 1

        digits_as_chars = str(integer_value)
        digits_as_numbers = [int(ch) for ch in digits_as_chars]
        digits_as_numbers[0] = digits_as_numbers[0] + sign_multiplier - 1

        total = 0
        index = 0
        while index < len(digits_as_numbers):
            total += digits_as_numbers[index]
            index += 1
        return total

    digit_sums_collected: List[int] = []
    idx = 0
    while idx < len(array_of_integers):
        digit_sums_collected.append(digits_sum(array_of_integers[idx]))
        idx += 1

    positive_only_sums: List[int] = []
    iter_ = 0
    while iter_ < len(digit_sums_collected):
        if digit_sums_collected[iter_] > 0:
            positive_only_sums.append(digit_sums_collected[iter_])
        iter_ += 1

    return len(positive_only_sums)