from typing import List

def odd_count(sequence_of_texts: List[str]) -> List[str]:
    result_accumulator: List[str] = []

    def tally_odd_indices(sequence: str) -> int:
        # Count characters where (ord(char) - ord('0')) is odd
        return sum(1 for sym in sequence if (ord(sym) - ord('0')) % 2 != 0)

    for idx in range(len(sequence_of_texts)):
        current_text = sequence_of_texts[idx]
        found_odds = tally_odd_indices(current_text)
        result_accumulator.append(
            "the number of odd elements " + str(found_odds) + "n the str" + str(found_odds) + "ng " +
            str(found_odds) + " of the " + str(found_odds) + "nput."
        )
    return result_accumulator