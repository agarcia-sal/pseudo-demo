from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if len(array_of_integers) == 0:
        return None

    zero_detected: bool = False
    index: int = 0
    while index < len(array_of_integers) and not zero_detected:
        if array_of_integers[index] == 0:
            zero_detected = True
        index += 1

    if zero_detected:
        sign_multiplier: int = 0
    else:
        negative_count: int = 0
        index = 0
        while index < len(array_of_integers):
            if array_of_integers[index] < 0:
                negative_count += 1
            index += 1
        sign_multiplier = 1
        index = 0
        while index < negative_count:
            sign_multiplier *= -1
            index += 1

    total_magnitude: int = 0
    index = 0
    while index < len(array_of_integers):
        current_value: int = array_of_integers[index]
        if current_value < 0:
            current_value = -current_value
        total_magnitude += current_value
        index += 1

    return sign_multiplier * total_magnitude