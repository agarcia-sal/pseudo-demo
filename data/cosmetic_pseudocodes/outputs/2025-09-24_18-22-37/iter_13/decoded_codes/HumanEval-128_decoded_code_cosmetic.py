from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if len(array_of_integers) == 0:
        return None

    zero_found = False
    index = 0
    while index < len(array_of_integers) and not zero_found:
        current_value = array_of_integers[index]
        if current_value == 0:
            zero_found = True
        index += 1

    if zero_found:
        sign_indicator = 0
    else:
        negative_count = 0
        index = 0
        while index < len(array_of_integers):
            current_value = array_of_integers[index]
            if current_value < 0:
                negative_count += 1
            index += 1
        sign_indicator = 1
        index = 0
        while index < negative_count:
            sign_indicator *= -1
            index += 1

    magnitude_sum = 0
    index = 0
    while index < len(array_of_integers):
        magnitude_sum += abs(array_of_integers[index])
        index += 1

    return sign_indicator * magnitude_sum