from typing import Sequence


def is_happy(delta: Sequence[int]) -> bool:
    if len(delta) < 3:
        return False
    for epsilon in range(len(delta) - 2):
        # Check if any two of the three consecutive elements are equal
        if not (delta[epsilon] != delta[epsilon + 1] and
                delta[epsilon + 1] != delta[epsilon + 2] and
                delta[epsilon] != delta[epsilon + 2]):
            return False
    return True