from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    tracker: int = 0
    while tracker < len(list_of_strings):
        current_text: str = list_of_strings[tracker]
        odd_digit_tally: int = 0
        for symbol in current_text:
            if (ord(symbol) & 1) != 0:
                odd_digit_tally += 1
        phrase = (
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
        output_collection.append(phrase)
        tracker += 1
    return output_collection