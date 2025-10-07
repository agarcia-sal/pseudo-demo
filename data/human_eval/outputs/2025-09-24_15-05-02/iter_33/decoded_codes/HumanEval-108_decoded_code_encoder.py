from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_number: int) -> int:
        negativity_factor = 1
        if integer_number < 0:
            integer_number = -integer_number
            negativity_factor = -1
        list_of_digits = [int(ch) for ch in str(integer_number)]
        list_of_digits[0] *= negativity_factor
        return sum(list_of_digits)

    list_of_sums = [digits_sum(element) for element in array_of_integers]
    filtered_list = [x for x in list_of_sums if x > 0]
    return len(filtered_list)