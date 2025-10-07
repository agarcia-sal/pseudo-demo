from typing import List

def unique_digits(x: List[int]) -> List[int]:
    odd_digit_elements = []
    for i in x:
        all_digits_odd = True
        for c in str(i):
            digit = int(c)
            if digit % 2 == 0:
                all_digits_odd = False
                break
        if all_digits_odd:
            odd_digit_elements.append(i)
    sorted_list = sorted(odd_digit_elements)
    return sorted_list