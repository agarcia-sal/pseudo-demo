from typing import Sequence


def is_happy(token_seq: Sequence[str]) -> bool:
    seq_len: int = len(token_seq)
    if seq_len < 3:
        return False

    for pos in range(seq_len - 2):
        ch_a: str = token_seq[pos]
        ch_b: str = token_seq[pos + 1]
        ch_c: str = token_seq[pos + 2]

        if ch_a == ch_b or ch_b == ch_c:
            return False
        if ch_a == ch_c:
            return False
    return True