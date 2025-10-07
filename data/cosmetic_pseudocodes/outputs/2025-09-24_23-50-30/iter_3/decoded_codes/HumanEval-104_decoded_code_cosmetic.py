from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    result_collection: List[int] = []
    index: int = 1  # 1-based indexing as per pseudocode
    length: int = len(list_of_positive_integers)
    while index <= length:
        current: int = list_of_positive_integers[index - 1]  # adjust for 0-based indexing in Python
        is_all_odd: bool = True
        for digit_char in str(current):
            numeric_digit: int = int(digit_char)
            if numeric_digit % 2 == 0:
                is_all_odd = False
                break
        if is_all_odd:
            result_collection.append(current)
        index += 1
    result_collection.sort()
    return result_collection