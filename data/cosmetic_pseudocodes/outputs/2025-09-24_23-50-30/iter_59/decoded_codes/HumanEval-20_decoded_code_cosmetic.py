from typing import Iterable, Optional, Sequence, Tuple

def find_closest_elements(a: Iterable[Tuple[int, int]]) -> Optional[Sequence[int]]:
    b: Optional[Sequence[int]] = None
    c: Optional[int] = None
    # Iterate over all pairs (d,e) and (f,g) in a
    for d, e in a:
        for f, g in a:
            if d != f:
                h = abs(e - g)
                if c is None or h < c:
                    b = sorted((e, g))
                    c = h
    return b