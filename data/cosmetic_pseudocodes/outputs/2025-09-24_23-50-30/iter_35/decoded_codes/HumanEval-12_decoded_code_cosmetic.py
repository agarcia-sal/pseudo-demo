from functools import reduce
from typing import Iterable, Optional

def longest(collection_of_texts: Iterable[str]) -> Optional[str]:
    texts = list(collection_of_texts)
    if not texts:
        return None

    max_len_var = reduce(
        lambda accum, curr: len(curr) if len(curr) > accum else accum,
        texts,
        0,
    )

    def find_match(items: list[str], target: int) -> Optional[str]:
        idx_var = 0
        while idx_var < len(items):
            if len(items[idx_var]) == target:
                return items[idx_var]
            idx_var += 1
        return None

    return find_match(texts, max_len_var)