from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            sign = -1

        digits_str = str(integer_value)
        digits_array: List[int] = [int(d) for d in digits_str]
        digits_array[0] = digits_array[0] * sign

        total = sum(digits_array)
        return total

    result_list: List[int] = []
    index = 0
    while index < len(array_of_integers):
        current_number = array_of_integers[index]
        result_list.append(digits_sum(current_number))
        index += 1

    positive_elements = [val for val in result_list if val > 0]

    return len(positive_elements)