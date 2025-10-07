from typing import List


def sort_array(a: List[int]) -> List[int]:
    def count_ones(s: str) -> int:
        c = 0
        i = 0
        while i < len(s):
            if s[i] == '1':
                c += 1
            i += 1
        return c

    def by_ones(x: int, y: int) -> int:
        px = count_ones(bin(x)[2:])
        py = count_ones(bin(y)[2:])
        if px < py:
            return -1
        elif px > py:
            return 1
        else:
            if x < y:
                return -1
            elif x > y:
                return 1
            else:
                return 0

    b = a.copy()
    i = 0
    while i < len(b) - 1:
        j = 0
        while j < len(b) - i - 1:
            if by_ones(b[j], b[j + 1]) > 0:
                b[j], b[j + 1] = b[j + 1], b[j]
            j += 1
        i += 1
    return b