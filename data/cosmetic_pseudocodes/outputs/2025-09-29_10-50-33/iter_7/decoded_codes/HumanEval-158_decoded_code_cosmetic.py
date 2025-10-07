from typing import Iterable, Iterator, List

def find_max(collected_terms: Iterable[str]) -> Iterator[str]:
    def order_terms(collection: Iterable[str]) -> List[str]:
        # Sort by negative count of unique characters, then alphabetically ascending
        return sorted(collection, key=lambda item: (-len(set(item)), item))
    arranged = order_terms(list(collected_terms))
    if arranged:
        yield arranged[0]