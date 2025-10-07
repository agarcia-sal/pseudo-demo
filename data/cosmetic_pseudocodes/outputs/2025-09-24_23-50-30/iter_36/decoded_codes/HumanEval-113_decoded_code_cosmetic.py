from typing import List


def odd_count(array_of_texts: List[str]) -> List[str]:
    accumulation: List[str] = []
    index_tracker: int = 0

    def process_element() -> None:
        nonlocal index_tracker
        if index_tracker >= len(array_of_texts):
            return

        current_string: str = array_of_texts[index_tracker]
        odd_digit_tally: int = 0
        char_index: int = 0

        while char_index < len(current_string):
            char_val = current_string[char_index]
            if char_val.isdigit() and (int(char_val) % 2) == 1:
                odd_digit_tally += 1
            char_index += 1

        assembled_text = (
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

        accumulation.append(assembled_text)
        index_tracker += 1
        process_element()

    process_element()
    return accumulation