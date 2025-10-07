from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier = -1

        digit_chars = str(integer_value)
        digit_values = [int(char) for char in digit_chars]
        digit_values[0] *= multiplier

        total = sum(digit_values)
        return total

    temp_results: List[int] = []
    index = 0

    while index < len(array_of_integers):
        current_value = array_of_integers[index]
        temp_results.append(digits_sum(current_value))
        index += 1

    def count_positive(values_list: List[int]) -> int:
        count = 0
        position = 0
        while position < len(values_list):
            if values_list[position] <= 0:
                position += 1
                continue
            count += 1
            position += 1
        return count

    return count_positive(temp_results)