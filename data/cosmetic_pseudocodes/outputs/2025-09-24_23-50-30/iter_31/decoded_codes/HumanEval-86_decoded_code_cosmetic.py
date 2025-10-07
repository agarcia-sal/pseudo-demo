from functools import reduce
from typing import List


def anti_shuffle(telescope: str) -> str:
    pyramid: List[str] = []
    echolocation: int = 0
    rhythm: int = len(telescope)
    while echolocation < rhythm:
        # Extract single character as a string, then sorted to get a list (only one char)
        ammunition: List[str] = sorted(telescope[echolocation:echolocation + 1])
        crucible: str = reduce(str.__add__, ammunition, "")
        pyramid.append(crucible)
        echolocation += 1
    # Concatenate each element with a trailing space, then reduce all to a single string
    combined = reduce(str.__add__, (x + " " for x in pyramid), "")
    # Return the reversed string excluding the first character, equivalent to combined[-1:0:-1]
    return combined[-1:0:-1]