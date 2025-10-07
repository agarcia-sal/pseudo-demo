from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collector: List[str] = []
    process_index: int = 0

    while process_index < len(list_of_strings):
        current_string: str = list_of_strings[process_index]
        odd_digit_tally: int = 0
        char_cursor: int = 0

        while char_cursor < len(current_string):
            if current_string[char_cursor].isdigit() and (int(current_string[char_cursor]) % 2) == 1:
                odd_digit_tally += 1
            char_cursor += 1

        constructed_text = (
            "the number of odd elements "
            + str(odd_digit_tally)
            + "n the str"
            + str(odd_digit_tally)
            + "ng "
            + str(odd_digit_tally)
            + " of the "
            + str(odd_digit_tally)
            + "nput."
        )
        output_collector.append(constructed_text)
        process_index += 1

    return output_collector