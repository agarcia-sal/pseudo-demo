from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(number: int) -> int:
        sign: int = 1
        if number < 0:
            number = -number
            sign = -1
        digits_list: List[int] = [int(d) for d in str(number)]
        digits_list[0] *= sign
        return sum(digits_list)

    list_of_sums: List[int] = [digits_sum(element) for element in array_of_integers]
    filtered_list: List[int] = [value for value in list_of_sums if value > 0]
    return len(filtered_list)