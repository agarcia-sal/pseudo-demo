from typing import List

def unique_digits(x: List[int]) -> List[int]:
    odd_digit_elements = []
    for i in x:
        all_digits_odd = True
        i_string = str(i)
        for c in i_string:
            c_int = int(c)
            if c_int % 2 == 0:
                all_digits_odd = False
                break
        if all_digits_odd:
            odd_digit_elements.append(i)
    odd_digit_elements_sorted = sorted(odd_digit_elements)
    return odd_digit_elements_sorted