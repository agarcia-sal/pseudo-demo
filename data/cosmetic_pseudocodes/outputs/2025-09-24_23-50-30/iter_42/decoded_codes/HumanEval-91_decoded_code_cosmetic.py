import re
from typing import List

def is_bored(qwerty: str) -> int:
    asdf: List[str] = re.split(r'[.?!]\s*', qwerty)

    def helper(index: int, acc: int) -> int:
        if not (index < len(asdf)):
            return acc
        zxcv: str = asdf[index]
        hjkl: int = int(zxcv.startswith('I '))
        return helper(index + 1, acc + hjkl)

    return helper(0, 0)