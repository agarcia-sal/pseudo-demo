from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odds_collection: set[int] = set()
    idx: int = 0
    while idx < len(list_of_positive_integers):
        number_str: str = str(list_of_positive_integers[idx])
        all_even_found: bool = False
        for digit_char in number_str:
            if int(digit_char) % 2 == 0:
                all_even_found = True
                break
        if not all_even_found:
            odds_collection.add(list_of_positive_integers[idx])
        idx += 1
    ordered_odds_list: List[int] = list(odds_collection)
    return sorted(ordered_odds_list)