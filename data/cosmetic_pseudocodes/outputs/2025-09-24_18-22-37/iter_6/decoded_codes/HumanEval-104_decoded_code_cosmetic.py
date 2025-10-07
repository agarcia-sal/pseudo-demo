from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    filtered_numbers: List[int] = []
    counter: int = 0
    while counter < len(list_of_positive_integers):
        current_num: int = list_of_positive_integers[counter]
        position: int = 0
        has_only_odd: bool = True
        current_num_str = str(current_num)
        while position < len(current_num_str):
            digit_char: str = current_num_str[position]
            digit_val: int = int(digit_char)
            if digit_val % 2 == 0:
                has_only_odd = False
                break
            position += 1
        if has_only_odd:
            filtered_numbers.append(current_num)
        counter += 1
    return sorted(filtered_numbers)