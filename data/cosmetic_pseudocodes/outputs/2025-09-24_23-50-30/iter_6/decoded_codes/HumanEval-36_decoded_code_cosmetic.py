from typing import List

def fizz_buzz(integer_n: int) -> int:
    collected_vals: List[int] = []
    idx: int = 0
    while idx < integer_n:
        if idx % 11 == 0 or idx % 13 == 0:
            collected_vals.append(idx)
        idx += 1

    combined: str = ""
    pos: int = 0
    while pos < len(collected_vals):
        combined += str(collected_vals[pos])
        pos += 1

    tally: int = 0
    loc: int = 0
    while loc < len(combined):
        if combined[loc] == '7':
            tally += 1
        loc += 1

    return tally