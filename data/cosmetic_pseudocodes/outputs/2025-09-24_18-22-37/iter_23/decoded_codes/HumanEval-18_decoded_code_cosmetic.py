from typing import Literal

def how_many_times(p_string: str, q_substr: str) -> int:
    tally: int = 0
    limit: int = len(p_string) - len(q_substr)
    pos: int = 0
    while pos <= limit:
        segment: str = p_string[pos:pos + len(q_substr)]
        if segment == q_substr:
            tally += 1  # (1 + 0) simplified
        pos += 1
    return tally