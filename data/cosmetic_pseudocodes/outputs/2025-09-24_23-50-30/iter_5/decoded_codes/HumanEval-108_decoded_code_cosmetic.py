from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        if integer_value >= 0:
            sign_factor = 1
        else:
            integer_value = -integer_value
            sign_factor = -1

        digit_chars = str(integer_value)
        digit_values = []
        for idx, ch in enumerate(digit_chars):
            if idx == 0:
                digit_values.append(sign_factor * int(ch))
            else:
                digit_values.append(int(ch))

        total_sum = sum(digit_values)
        return total_sum

    temp_sums = map(digits_sum, array_of_integers)
    positive_sums = [v for v in temp_sums if v > 0]
    return len(positive_sums)