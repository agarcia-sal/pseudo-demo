from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=str)

def filter_by_prefix(container_of_items: Iterable[T], initial_segment: str) -> List[T]:
    result_collection: List[T] = []
    current_index: int = 0
    items = list(container_of_items)  # Ensure indexing and length support
    while current_index < len(items):
        candidate_item = items[current_index]
        if not candidate_item.startswith(initial_segment):
            current_index += 1
            continue
        result_collection.append(candidate_item)
        current_index += 1
    return result_collection