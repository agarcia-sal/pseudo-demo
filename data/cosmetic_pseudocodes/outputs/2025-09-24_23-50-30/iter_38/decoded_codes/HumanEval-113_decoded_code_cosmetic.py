from typing import List

def odd_count(array_of_tokens: List[str]) -> List[str]:
    aggregate: List[str] = []
    for element in array_of_tokens:
        tally: int = sum(1 for character in element if int(character) % 2 == 1)
        aggregate.append(
            f"the number of odd elements {tally}n the str{tally}ng {tally} of the {tally}nput."
        )
    return aggregate