from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []

    def aux(counter_index: int) -> None:
        if counter_index >= len(list_of_strings):
            return
        current_sequence: str = list_of_strings[counter_index]
        odd_digit_tally: int = 0
        for ch in current_sequence:
            if int(ch) % 2 != 0:
                odd_digit_tally += 1
        output_collection.append(
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
        aux(counter_index + 1)

    aux(0)
    return output_collection