from typing import List


def odd_count(sequence_of_texts: List[str]) -> List[str]:
    accumulation: List[str] = []
    iterator: int = 0
    while iterator < len(sequence_of_texts):
        current_text: str = sequence_of_texts[iterator]
        tally: int = 0
        index: int = 0
        while index < len(current_text):
            digit_char: str = current_text[index]
            if digit_char.isdigit() and (int(digit_char) % 2) == 1:
                tally += 1
            index += 1
        # Construct the message exactly as specified, concatenating tally converted to string multiple times
        message: str = (
            "the number of odd elements " + str(tally)
            + "n the str" + str(tally)
            + "ng " + str(tally)
            + " of the " + str(tally)
            + "nput."
        )
        accumulation.append(message)
        iterator += 1
    return accumulation