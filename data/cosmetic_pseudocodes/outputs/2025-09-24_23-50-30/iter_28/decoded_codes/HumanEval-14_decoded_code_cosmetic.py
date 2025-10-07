from typing import List

def all_prefixes(seed: str) -> List[str]:
    def iterator(pos: int, acc: List[str]) -> List[str]:
        if pos < 0:
            return acc
        else:
            return iterator(pos - 1, [seed[: pos + 1]] + acc)
    return iterator(len(seed) - 1, [])