from typing import List, Dict


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    accumulator: Dict[int, bool] = {}

    def check_oddities(index: int) -> None:
        if index == len(list_of_positive_integers):
            return
        candidate = list_of_positive_integers[index]
        digit_string = str(candidate)
        is_odd = True
        position = 0
        while position < len(digit_string) and is_odd:
            numeric_val = ord(digit_string[position]) - ord('0')
            is_even = (numeric_val % 2) == 0
            is_odd = not is_even
            position += 1
        if is_odd:
            accumulator[candidate] = True
        check_oddities(index + 1)

    check_oddities(0)
    result_list = sorted(accumulator.keys())
    return result_list