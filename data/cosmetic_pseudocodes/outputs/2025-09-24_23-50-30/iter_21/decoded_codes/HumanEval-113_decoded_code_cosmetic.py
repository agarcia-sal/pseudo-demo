from typing import List

def odd_count(input_array: List[str]) -> List[str]:
    output_collection: List[str] = []

    def count_odds_in_text(text: str, idx: int, acc: int) -> int:
        if idx == len(text):
            return acc
        numeric_val = int(text[idx])
        increment = 1 if numeric_val % 2 == 1 else 0
        return count_odds_in_text(text, idx + 1, acc + increment)

    for element_index in range(len(input_array)):
        current_string = input_array[element_index]
        odd_digit_count = count_odds_in_text(current_string, 0, 0)

        constructed_message = (
            "the number of odd elements "
            + str(odd_digit_count)
            + "n the str"
            + str(odd_digit_count)
            + "ng "
            + str(odd_digit_count)
            + " of the "
            + str(odd_digit_count)
            + "nput."
        )
        output_collection.append(constructed_message)

    return output_collection