from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(number: int) -> int:
        factor = 1
        if number < 0:
            number = -number
            factor = -1
        digits_string = str(number)
        digits_list: List[int] = []
        index = 0
        while index < len(digits_string):
            char = digits_string[index]
            digit = int(char)
            digits_list.append(digit)
            index += 1
        if len(digits_list) >= 2:
            digits_list[1] = digits_list[1] * factor
        total = 0
        i = 0
        while i < len(digits_list):
            total += digits_list[i]
            i += 1
        return total

    sums_collection: List[int] = []
    idx = 0
    while idx < len(array_of_integers):
        current_num = array_of_integers[idx]
        sum_of_digits = digits_sum(current_num)
        sums_collection.append(sum_of_digits)
        idx += 1

    filtered_sums: List[int] = []
    j = 0
    while j < len(sums_collection):
        element = sums_collection[j]
        if element > 0:
            filtered_sums.append(element)
        j += 1

    result_count = len(filtered_sums)
    return result_count