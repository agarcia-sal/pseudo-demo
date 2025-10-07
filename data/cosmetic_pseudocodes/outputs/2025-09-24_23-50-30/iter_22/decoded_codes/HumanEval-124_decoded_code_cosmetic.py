from typing import List


def valid_date(alpha: str) -> bool:
    # Remove all whitespace characters from the input string
    def trim(s: str) -> str:
        return ''.join(c for c in s if c not in {' ', '\t', '\n'})

    parts = trim(alpha).split('-')
    if len(parts) != 3:
        return False

    ordinals: List[int] = []
    for element in parts:
        try:
            ordinals.append(int(element))
        except ValueError:
            return False

    m, d, y = ordinals

    if m < 1 or m > 12:
        return False

    if m == 2:
        if d < 1 or d > 29:
            return False
    elif m in {4, 6, 9, 11}:
        if d < 1 or d > 30:
            return False
    else:
        if d < 1 or d > 31:
            return False

    return True