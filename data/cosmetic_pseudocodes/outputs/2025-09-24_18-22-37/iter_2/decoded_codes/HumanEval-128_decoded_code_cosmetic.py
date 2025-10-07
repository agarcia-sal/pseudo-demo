from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if len(array_of_integers) == 0:
        return None

    zero_found = False
    negative_tot = 0

    for each_element in array_of_integers:
        if each_element == 0:
            zero_found = True
            break
        elif each_element < 0:
            negative_tot += 1

    sign_product = 0 if zero_found else (-1) ** negative_tot

    sum_of_magnitudes = sum(abs(val) for val in array_of_integers)

    return sign_product * sum_of_magnitudes