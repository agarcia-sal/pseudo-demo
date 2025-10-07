from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier_sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier_sign = -1

        digit_sequence = [int(ch) for ch in str(integer_value)]
        digit_sequence[0] *= multiplier_sign

        total_sum = sum(digit_sequence)
        return total_sum

    sums_list: List[int] = []

    def process_element(index: int) -> None:
        if index == len(array_of_integers):
            return
        current_value = array_of_integers[index]
        sums_list.append(digits_sum(current_value))
        process_element(index + 1)

    process_element(0)

    positive_sums = [item for item in sums_list if item > 0]

    return len(positive_sums)