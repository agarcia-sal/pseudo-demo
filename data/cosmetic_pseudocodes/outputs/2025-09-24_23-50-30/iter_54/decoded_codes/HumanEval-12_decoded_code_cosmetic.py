from typing import Iterable, Optional, TypeVar, List

T = TypeVar('T', bound=Iterable)

def longest(collection: Iterable[Iterable]) -> Optional[Iterable]:
    def find_maximum_length(current_max: int, remaining_items: List[Iterable]) -> int:
        if not remaining_items:
            return current_max
        head, tail = remaining_items[0], remaining_items[1:]
        candidate = len(head)
        # Update current_max if candidate is greater
        return find_maximum_length(candidate if candidate > current_max else current_max, tail)

    items = list(collection)
    if not items:
        return None

    max_len = find_maximum_length(0, items)

    def search_longest_item(items: List[Iterable]) -> Optional[Iterable]:
        if not items:
            return None
        current_item, rest_items = items[0], items[1:]
        return current_item if len(current_item) == max_len else search_longest_item(rest_items)

    return search_longest_item(items)