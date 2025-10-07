from typing import Iterable, Optional

def next_smallest(collection_of_numbers: Iterable[int]) -> Optional[int]:
    s = set(collection_of_numbers)  # remove duplicates
    A = sorted(s)
    if len(A) < 2:
        return None
    else:
        return A[1]