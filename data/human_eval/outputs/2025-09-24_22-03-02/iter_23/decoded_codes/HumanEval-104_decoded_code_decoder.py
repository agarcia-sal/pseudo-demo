from typing import List

def unique_digits(x: List[int]) -> List[int]:
    odd_digit_elements = []
    index_x = 0
    while index_x < len(x):
        i = x[index_x]
        is_all_digits_odd = True
        str_i = str(i)
        index_c = 0
        while index_c < len(str_i):
            c = str_i[index_c]
            digit = int(c)
            if digit % 2 == 0:
                is_all_digits_odd = False
                break
            index_c += 1
        if is_all_digits_odd == True:
            odd_digit_elements.append(i)
        index_x += 1
    odd_digit_elements.sort()
    return odd_digit_elements