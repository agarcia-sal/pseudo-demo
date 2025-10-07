from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    collected_odds: List[int] = []
    index_counter: int = 0
    while index_counter < len(list_of_positive_integers):
        current_number: int = list_of_positive_integers[index_counter]
        has_only_odd_digits: bool = True
        for character in str(current_number):
            digit_value: int = int(character)
            if digit_value % 2 == 0:
                has_only_odd_digits = False
                break
        if has_only_odd_digits:
            collected_odds.append(current_number)
        index_counter += 1
    collected_odds.sort()
    return collected_odds