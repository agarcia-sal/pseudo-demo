from typing import List


def odd_count(input_collection: List[str]) -> List[str]:
    accumulator: List[str] = []

    c: int = 0
    while c < len(input_collection):
        current_str: str = input_collection[c]

        def count_odds(index: int, acc: int) -> int:
            if index == len(current_str):
                return acc
            ch = current_str[index]
            val = int(ch)
            if val % 2 == 1:
                return count_odds(index + 1, acc + 1)
            else:
                return count_odds(index + 1, acc)

        odd_tally = count_odds(0, 0)

        composed_str = (
            "the number of odd elements "
            + str(odd_tally)
            + "n the str"
            + str(odd_tally)
            + "ng "
            + str(odd_tally)
            + " of the "
            + str(odd_tally)
            + "nput."
        )

        accumulator.append(composed_str)
        c += 1

    return accumulator