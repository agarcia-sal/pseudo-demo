from typing import List

def unique_digits(x: List[int]) -> List[int]:
    odd_digit_elements = []
    for index_i in range(len(x)):
        i = x[index_i]
        all_digits_odd = True
        string_i = str(i)
        for index_c in range(len(string_i)):
            c = string_i[index_c]
            digit = int(c)
            if digit % 2 == 0:
                all_digits_odd = False
                break
        if all_digits_odd:
            odd_digit_elements.append(i)
    sorted_result = sorted(odd_digit_elements)
    return sorted_result