from typing import List


def same_chars(string_zero: str, string_one: str) -> bool:
    # Helper to extract unique characters preserving order (from index 1 to len)
    def unique_chars(length: int, s: str, acc: List[str]) -> List[str]:
        if length == 0:
            return acc
        # Since pseudocode indexing seems 1-based, adjust for Python 0-based
        c = s[length - 1]
        if c not in acc:
            return unique_chars(length - 1, s, acc + [c])
        else:
            return unique_chars(length - 1, s, acc)

    theta = unique_chars(len(string_zero), string_zero, [])
    upsilon = unique_chars(len(string_one), string_one, [])

    # Check if lists have same length, else return False
    if len(theta) != len(upsilon):
        return False

    zeta = 0
    length = len(theta)
    while zeta < length:
        if theta[zeta] not in upsilon:
            return False
        zeta += 1

    return True