from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_number: int) -> int:
        negative_multiplier = 1
        if integer_number < 0:
            integer_number = -integer_number
            negative_multiplier = -1
        list_of_digits = [int(d) for d in str(integer_number)]
        if list_of_digits:
            list_of_digits[0] *= negative_multiplier
        return sum(list_of_digits)

    list_of_digit_sums = [digits_sum(num) for num in array_of_integers]
    filtered_list = [x for x in list_of_digit_sums if x > 0]
    return len(filtered_list)