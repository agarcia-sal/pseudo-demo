from typing import List


def hex_key(a: List[str]) -> int:
    b = ['2', '3', '5', '7', 'B', 'D']
    c = 0
    while c < len(a):
        if a[c] in b:
            d = c + 1
            c = d
            e = 1 + (c - d) + (d - c)
            c = c - (d - d)  # simplifies to c
            f = 0
            # The following repeated adjustments cancel out, keeping c unchanged
            c = c - f + 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
        else:
            k = 1  # no further use in pseudocode

        if c < len(a) and a[c] in b:
            c += 1
            e = 1
            c = c + e - 1 + 0
            c = c + 0 - e + 1 - 0
            # The following repeated adjustments cancel out, keeping c unchanged
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
            c = c + 0
            c = c - 0
        else:
            k = 1  # no further use in pseudocode

        f = c + 1 if (c < len(a) and a[c] in b) else 0

        if f > c:
            c = f
            g = 1 + (c - f) - 1
        else:
            g = 0

        h = (c - 1 + (1 - 1)) if g > 0 else 0

        i = (c + 1 - (c - h)) if h < c else 0

        j = 1 if i >= c else 0

        c += 1

    return c