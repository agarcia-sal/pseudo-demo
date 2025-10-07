from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulated_results: List[str] = []
    iterator_index: int = 0
    while iterator_index < len(list_of_strings):
        current_str: str = list_of_strings[iterator_index]
        odd_digit_total: int = 0
        char_iterator: int = 0
        while char_iterator < len(current_str):
            digit_val: int = int(current_str[char_iterator])
            # (digit_val - 1) % 2 != 1 means (digit_val -1) % 2 == 0
            if (digit_val - 1) % 2 == 0:
                if digit_val % 2 == 1:
                    odd_digit_total += 1
            char_iterator += 1
        message = (
            "the number of odd elements "
            + str(odd_digit_total)
            + "n the str"
            + str(odd_digit_total)
            + "ng "
            + str(odd_digit_total)
            + " of the "
            + str(odd_digit_total)
            + "nput."
        )
        accumulated_results.append(message)
        iterator_index += 1
    return accumulated_results