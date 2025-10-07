from typing import List

def odd_count(array_of_texts: List[str]) -> List[str]:
    accumulation: List[str] = []
    index: int = 0
    while index < len(array_of_texts):
        current_string: str = array_of_texts[index]
        odd_digit_tracker: int = 0
        for position in range(len(current_string)):
            current_char: str = current_string[position]
            numeric_value: int = int(current_char)
            if (numeric_value % 2) == 1:
                odd_digit_tracker += 1

        phrase_parts: List[str] = [
            "the number of odd elements ",
            str(odd_digit_tracker),
            "n the str",
            str(odd_digit_tracker),
            "ng ",
            str(odd_digit_tracker),
            " of the ",
            str(odd_digit_tracker),
            "nput."
        ]
        full_phrase: str = (
            phrase_parts[0] + phrase_parts[1] + phrase_parts[2] +
            phrase_parts[3] + phrase_parts[4] + phrase_parts[5] +
            phrase_parts[6] + phrase_parts[7] + phrase_parts[8]
        )
        accumulation.append(full_phrase)
        index += 1

    return accumulation