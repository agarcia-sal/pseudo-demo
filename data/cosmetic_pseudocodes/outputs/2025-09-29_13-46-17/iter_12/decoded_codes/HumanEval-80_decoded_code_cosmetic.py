from typing import Tuple


def is_happy(string_input: str) -> bool:
    length: int = len(string_input)
    if length < 3:
        return False
    # Iterate over all triplets starting indices
    for idx in range(length - 2):
        triplet: Tuple[str, str, str] = (
            string_input[idx],
            string_input[idx + 1],
            string_input[idx + 2],
        )
        # Check if any two chars in the triplet are equal
        if not (triplet[0] == triplet[1] or triplet[1] == triplet[2] or triplet[0] == triplet[2]):
            return False
    return True