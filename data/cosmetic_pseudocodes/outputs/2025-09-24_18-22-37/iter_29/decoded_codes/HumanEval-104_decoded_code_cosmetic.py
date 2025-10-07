from typing import List


def unique_digits(vault_of_naturals: List[int]) -> List[int]:
    collection_of_odds: List[int] = []
    cursor: int = 0
    while cursor < len(vault_of_naturals):
        current_value = vault_of_naturals[cursor]
        index_in_number = 0
        is_all_odd = True
        digits_str = str(abs(current_value))  # Handle negative numbers gracefully if any
        while index_in_number < len(digits_str) and is_all_odd:
            digit_value = int(digits_str[index_in_number])
            if digit_value % 2 != 1:  # digit_value is not odd
                is_all_odd = False
            else:
                index_in_number += 1
        if is_all_odd:
            collection_of_odds.append(current_value)
        cursor += 1
    return sorted(collection_of_odds)