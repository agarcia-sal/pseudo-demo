from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        if integer_value < 0:
            integer_value = -integer_value
            sign_multiplier = -1
        else:
            sign_multiplier = 1

        digit_chars = str(integer_value)
        digits_array: List[int] = [int(d) for d in digit_chars]

        digits_array[0] *= sign_multiplier

        total_sum = 0
        iterator = 0
        length = len(digits_array)
        while iterator < length:
            total_sum += digits_array[iterator]
            iterator += 1
        return total_sum

    transformed_sums: List[int] = []
    iterator_outer = 0
    length_outer = len(array_of_integers)
    while iterator_outer < length_outer:
        current_element = array_of_integers[iterator_outer]
        summed_digits = digits_sum(current_element)
        transformed_sums.append(summed_digits)
        iterator_outer += 1

    count_positive = 0
    for element in transformed_sums:
        if element > 0:
            count_positive += 1

    return count_positive