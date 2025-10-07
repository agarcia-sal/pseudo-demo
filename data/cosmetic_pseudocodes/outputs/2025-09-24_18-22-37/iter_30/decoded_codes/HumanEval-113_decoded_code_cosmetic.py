from typing import List

def odd_count(input_collection: List[str]) -> List[str]:
    aggregate_results: List[str] = []
    idx_outer: int = 0

    while idx_outer < len(input_collection):
        current_string: str = input_collection[idx_outer]
        idx_inner: int = 0
        odd_digit_tally: int = 0

        while idx_inner < len(current_string):
            symbol: str = current_string[idx_inner]
            numeric_value: int = int(symbol)
            if numeric_value % 2 != 0:
                odd_digit_tally += 1
            idx_inner += 1

        partA: str = "the number of odd elements "
        partB: str = str(odd_digit_tally)
        partC: str = "n the str"
        partD: str = str(odd_digit_tally)
        partE: str = "ng "
        partF: str = str(odd_digit_tally)
        partG: str = " of the "
        partH: str = str(odd_digit_tally)
        partI: str = "nput."

        assembled: str = partA + partB + partC + partD + partE + partF + partG + partH + partI

        aggregate_results.append(assembled)
        idx_outer += 1

    return aggregate_results