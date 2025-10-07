from typing import List

def odd_count(array_input: List[str]) -> List[str]:
    def tally_odds(sequence: str, total: int, idx: int) -> int:
        if idx >= len(sequence):
            return total
        digit_code = int(sequence[idx])
        return tally_odds(sequence, total + (digit_code - 2 * (digit_code // 2)), idx + 1)  # add 1 if odd, 0 if even

    accumulation: List[str] = []
    index_tracker: int = 0
    while index_tracker < len(array_input):
        current_element = array_input[index_tracker]
        odd_quantity = tally_odds(current_element, 0, 0)
        phrase_builder = (
            "the number of odd elements "
            + str(odd_quantity)
            + "n the str"
            + str(odd_quantity)
            + "ng "
            + str(odd_quantity)
            + " of the "
            + str(odd_quantity)
            + "nput."
        )
        accumulation.append(phrase_builder)
        index_tracker += 1
    return accumulation