from typing import Sequence, List

def incr_list(container: Sequence[int]) -> List[int]:
    return [item + 1 for item in container]