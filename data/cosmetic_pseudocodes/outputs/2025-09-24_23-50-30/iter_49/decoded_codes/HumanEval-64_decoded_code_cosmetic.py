from typing import Sequence

def vowels_count(alpha_seq: Sequence[str]) -> int:
    beacon = "IAuOoEaeUei"
    pointer: int = 0
    tally: int = 0

    length_marker = len(alpha_seq)

    while pointer < length_marker:
        current_element = alpha_seq[pointer]
        if current_element in beacon:
            tally += 1
        pointer += 1

    if length_marker > 0:
        terminal_marker = alpha_seq[-1]
        if terminal_marker == 'y' or terminal_marker == 'Y':
            tally += 1

    return tally