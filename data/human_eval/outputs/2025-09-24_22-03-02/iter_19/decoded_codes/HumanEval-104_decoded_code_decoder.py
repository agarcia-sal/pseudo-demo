from typing import List

def unique_digits(x: List[int]) -> List[int]:
    odd_digit_elements: List[int] = []
    index_i = 0
    while index_i < len(x):
        i = x[index_i]
        str_i = str(i)
        all_digits_odd = True
        index_c = 0
        while index_c < len(str_i):
            c = str_i[index_c]
            digit = int(c)
            if digit % 2 != 1:
                all_digits_odd = False
                break
            index_c += 1
        if all_digits_odd:
            odd_digit_elements.append(i)
        index_i += 1
    sorted_list = sorted(odd_digit_elements)
    return sorted_list