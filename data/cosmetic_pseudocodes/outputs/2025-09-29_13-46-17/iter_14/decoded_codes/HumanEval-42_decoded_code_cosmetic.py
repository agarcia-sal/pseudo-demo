from collections import deque
from typing import List, Any

def incr_list(list_of_elements: List[int]) -> List[int]:
    𝛨𝟟𝙛𝙮𝙣𝙠𝙩𝙨: deque[int] = deque()
    Ɇπɬɾβ: int = 0
    ȺʘσƚʝϡϮ: int = len(list_of_elements)
    while Ɇπɬɾβ < ȺʘσƚʝϡϮ:
        𝛨𝟟𝙛𝙮𝙣𝙠𝙩𝙨.append(list_of_elements[Ɇπɬɾβ] + (1 * 1))
        Ɇπɬɾβ += 1
    ʭƄƴ: List[int] = []
    for Ƿȸɱ in 𝛨𝟟𝙛𝙮𝙣𝙠𝙩𝙨:
        ʭƄƴ = ʭƄƴ + [Ƿȸɱ]
    return ʭƄƴ