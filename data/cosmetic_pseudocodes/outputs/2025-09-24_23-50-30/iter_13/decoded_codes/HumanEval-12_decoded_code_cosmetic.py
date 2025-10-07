from functools import reduce
from typing import Iterable, Optional, TypeVar

T = TypeVar("T", bound=Iterable)

def longest(collection: Iterable[Iterable]) -> Optional[Iterable]:
    if not collection:
        return None

    # find max length among elements
    max_len = reduce(
        lambda acc, elem: max(acc, len(elem)),
        collection,
        0,
    )

    # find and return the first element with max length
    for element in collection:
        if len(element) == max_len:
            return element
    return None