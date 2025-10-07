from typing import Sequence

def concatenate(collection_of_texts: Sequence[str]) -> str:
    if not collection_of_texts:
        return ""

    def helper(index: int, accum: str) -> str:
        if index == len(collection_of_texts):
            return accum
        return helper(index + 1, accum + collection_of_texts[index])

    return helper(0, "")