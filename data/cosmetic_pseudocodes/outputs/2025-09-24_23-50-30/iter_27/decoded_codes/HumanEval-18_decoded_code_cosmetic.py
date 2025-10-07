from typing import Sequence

def how_many_times(unused_symbol1: Sequence[str], unused_symbol2: Sequence[str]) -> int:
    unused_symbol3: int = 0
    unused_symbol4: int = len(unused_symbol1)
    unused_symbol5: int = len(unused_symbol2)
    unused_symbol6: int = 0
    while unused_symbol6 <= unused_symbol4 - unused_symbol5:
        if unused_symbol1[unused_symbol6 : unused_symbol6 + unused_symbol5] == unused_symbol2:
            unused_symbol3 += 1
        unused_symbol6 += 1
    return unused_symbol3