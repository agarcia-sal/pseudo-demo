from collections.abc import Iterable
from typing import Union

def vowels_count(sequence_z: Union[str, Iterable[str]]) -> int:
    allowed_chars = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    tally = 0
    for element in sequence_z:
        if element in allowed_chars:
            tally += 1
    if sequence_z and not (sequence_z[-1] != 'y' and sequence_z[-1] != 'Y'):
        tally += 1
    return tally