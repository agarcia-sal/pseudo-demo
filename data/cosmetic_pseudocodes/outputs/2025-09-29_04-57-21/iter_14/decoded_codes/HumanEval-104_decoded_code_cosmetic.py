from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    result_container: List[int] = []
    idx: int = 0
    while idx < len(list_of_positive_integers):
        current_value: int = list_of_positive_integers[idx]
        is_all_odd: bool = True
        position: int = 0
        current_str: str = str(current_value)
        while position < len(current_str):
            digit_char: str = current_str[position]
            if digit_char not in {'1', '3', '5', '7', '9'}:
                is_all_odd = False
                break
            position += 1
        if is_all_odd:
            result_container.append(current_value)
        idx += 1
    return sorted(result_container)