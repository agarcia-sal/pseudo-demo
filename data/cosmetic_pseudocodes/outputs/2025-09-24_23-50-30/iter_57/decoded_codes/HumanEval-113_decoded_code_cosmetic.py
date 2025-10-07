from typing import Collection, List

def odd_count(input_collection: Collection[str]) -> List[str]:
    aggregate: List[str] = []
    for idx in range(len(input_collection)):
        current_item: str = input_collection[idx]
        tally: int = 0
        for pos in range(len(current_item)):
            digit_char: str = current_item[pos]
            if int(digit_char) % 2 != 0:
                tally += 1
        phrase = (
            "the number of odd elements "
            + str(tally)
            + "n the str"
            + str(tally)
            + "ng "
            + str(tally)
            + " of the "
            + str(tally)
            + "nput."
        )
        aggregate.append(phrase)
    return aggregate