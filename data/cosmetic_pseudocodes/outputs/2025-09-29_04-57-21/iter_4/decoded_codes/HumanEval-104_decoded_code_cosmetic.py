from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    filtered_values: List[int] = []
    pos_index: int = 0
    while pos_index < len(list_of_positive_integers):
        candidate_number: int = list_of_positive_integers[pos_index]
        digit_checker: int = candidate_number
        only_odds: bool = True
        while digit_checker > 0 and only_odds:
            digit: int = digit_checker % 10
            if digit % 2 == 0:
                only_odds = False
            digit_checker //= 10
        if only_odds:
            filtered_values.append(candidate_number)
        pos_index += 1
    return sorted(filtered_values)