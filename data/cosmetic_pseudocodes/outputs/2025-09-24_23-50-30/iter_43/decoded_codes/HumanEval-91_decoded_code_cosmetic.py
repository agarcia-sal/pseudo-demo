import re
from typing import List


def is_bored(param_X: str) -> int:
    array_alpha: List[str] = re.split(r'[?!.]\s*', param_X)
    counter_beta: int = 0
    for fragment_delta in array_alpha:
        if len(fragment_delta) >= 2 and fragment_delta[:2] == 'I ':
            counter_beta += 1
    return counter_beta