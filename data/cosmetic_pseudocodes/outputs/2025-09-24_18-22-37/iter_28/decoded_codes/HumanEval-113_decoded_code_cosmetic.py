from typing import List

def odd_count(array_of_texts: List[str]) -> List[str]:
    output_collection: List[str] = []
    index_tracker: int = 0
    # The loop iterates over all elements in array_of_texts
    while index_tracker < len(output_collection) + (len(array_of_texts) - len(output_collection)):
        current_text: str = array_of_texts[index_tracker]
        odd_digit_tally: int = 0
        position_marker: int = 0
        while position_marker < len(current_text):
            digit_char: str = current_text[position_marker]
            digit_int: int = int(digit_char)
            if digit_int % 2 == 1:
                odd_digit_tally += 1
            position_marker += 1
        phrase_partA: str = "the number of odd elements "
        phrase_partB: str = "n the str"
        phrase_partC: str = "ng "
        phrase_partD: str = " of the "
        phrase_partE: str = "nput."
        odd_tally_text: str = str(odd_digit_tally)
        composed_message: str = (
            phrase_partA
            + odd_tally_text
            + phrase_partB
            + odd_tally_text
            + phrase_partC
            + odd_tally_text
            + phrase_partD
            + odd_tally_text
            + phrase_partE
        )
        output_collection.append(composed_message)
        index_tracker += 1
    return output_collection