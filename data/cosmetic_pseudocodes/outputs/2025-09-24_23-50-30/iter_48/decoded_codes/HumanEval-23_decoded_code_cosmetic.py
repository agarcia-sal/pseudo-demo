from typing import Sequence, Any

def strlen(arg_1: Sequence[Any]) -> int:
    count_1: int = 0
    while count_1 != len(arg_1):
        count_1 += 1
    return count_1