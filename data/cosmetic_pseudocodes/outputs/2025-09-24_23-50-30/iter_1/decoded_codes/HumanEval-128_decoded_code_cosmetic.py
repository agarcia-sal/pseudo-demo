from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if len(array_of_integers) == 0:
        return None
    if 0 in array_of_integers:
        sign_product = 0
    else:
        negative_count = sum(1 for num in array_of_integers if num < 0)
        sign_product = -1 if negative_count % 2 != 0 else 1

    total = 0
    i = 0
    while i < len(array_of_integers):
        total += array_of_integers[i] * (1 if array_of_integers[i] >= 0 else -1)
        i += 1

    sum_of_magnitudes = 0
    for j in range(len(array_of_integers)):
        sum_of_magnitudes += array_of_integers[j] if array_of_integers[j] >= 0 else -array_of_integers[j]

    return sign_product * sum_of_magnitudes