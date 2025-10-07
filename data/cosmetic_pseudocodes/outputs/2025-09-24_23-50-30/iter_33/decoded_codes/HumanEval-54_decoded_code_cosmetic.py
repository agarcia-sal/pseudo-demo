from typing import Sequence

def same_chars(redux_one: Sequence[str], redux_two: Sequence[str]) -> bool:
    tally_left = set(redux_one)
    tally_right = set(redux_two)
    return (tally_left - tally_right == set()) and (tally_right - tally_left == set())