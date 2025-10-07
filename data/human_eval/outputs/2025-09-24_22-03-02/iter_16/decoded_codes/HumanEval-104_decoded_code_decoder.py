from typing import List

def unique_digits(x: List[int]) -> List[int]:
    odd_digit_elements: List[int] = []
    for i in x:
        all_digits_odd = True
        string_i = str(i)
        for c in string_i:
            if int(c) % 2 == 0:
                all_digits_odd = False
                break
        if all_digits_odd:
            odd_digit_elements.append(i)
    sorted_result = sorted(odd_digit_elements)
    return sorted_result