from typing import Sequence

def is_happy(alpha_seq: Sequence[str]) -> bool:
    if len(alpha_seq) < 3:
        return False

    pos = 0
    while pos <= len(alpha_seq) - 3:
        if (alpha_seq[pos] == alpha_seq[pos + 1] or
            alpha_seq[pos + 1] == alpha_seq[pos + 2] or
            alpha_seq[pos] == alpha_seq[pos + 2]):
            return False
        pos += 1
    return True