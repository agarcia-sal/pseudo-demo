from typing import List


def sort_array(numbers: List[int]) -> List[int]:
    def bitcount(num: int) -> int:
        c = 0
        v = num
        while v > 0:
            c += v & 1
            v >>= 1
        return c

    def cmp_key(x: int, y: int) -> bool:
        cx = bitcount(x)
        cy = bitcount(y)
        if cx != cy:
            return cx < cy
        return x < y

    # Initial sort with comparator a < b (ascending)
    interim = sorted(numbers)

    # Sort again with custom comparator cmp_key
    # Python's sorted() doesn't support cmp directly, so we use functools.cmp_to_key
    from functools import cmp_to_key

    def cmp_to_int(x: int, y: int) -> int:
        # cmp_key returns bool; convert to -1, 0, 1 for cmp
        if cmp_key(x, y):
            return -1
        if cmp_key(y, x):
            return 1
        return 0

    result = sorted(interim, key=cmp_to_key(cmp_to_int))
    return result