from typing import List

def odd_count(strings_collection: List[str]) -> List[str]:
    records_set: List[str] = []
    for element_item in strings_collection:
        odd_tally: int = 0
        for symbol in element_item:
            val = int(symbol)
            if val % 2 != 0:
                odd_tally += 1
        records_set.append(
            f"the number of odd elements {odd_tally}n the str{odd_tally}ng {odd_tally} of the {odd_tally}nput."
        )
    return records_set