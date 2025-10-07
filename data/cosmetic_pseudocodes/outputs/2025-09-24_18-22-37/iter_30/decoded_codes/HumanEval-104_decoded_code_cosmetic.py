from typing import List


def unique_digits(array_of_numbers: List[int]) -> List[int]:
    special_collection: List[int] = []
    position: int = 0
    LENGTH: int = len(array_of_numbers)

    while position < LENGTH:
        element: int = array_of_numbers[position]
        is_all_odd: bool = True
        digit_str: str = str(element)
        index_char: int = 0
        len_char: int = len(digit_str)

        while index_char < len_char and is_all_odd:
            current_char: str = digit_str[index_char]
            current_digit: int = int(current_char)
            if current_digit % 2 == 0:
                is_all_odd = False
            index_char += 1

        if is_all_odd:
            special_collection.append(element)

        position += 1

    sorted_collection: List[int] = sorted(special_collection)
    return sorted_collection