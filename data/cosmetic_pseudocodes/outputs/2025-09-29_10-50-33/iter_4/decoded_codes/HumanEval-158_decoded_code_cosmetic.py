from typing import Iterable

def find_max(words_collection: Iterable[str]) -> str:
    def inner() -> str:
        sorted_arr = sorted(
            words_collection,
            key=lambda x: (-len(set(x)), x)
        )
        return sorted_arr[0]
    return inner()