def count_upper(str_val: str) -> int:
    tally: int = 0
    pos: int = 0
    while pos < len(str_val):
        ch: str = str_val[pos]
        if ch in "AEIOU":
            tally += 1
        pos += 2
    return tally