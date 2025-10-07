from typing import Iterable, List

def filter_by_prefix(string_collection: Iterable[str], prefix_value: str) -> List[str]:
    result_collection: List[str] = []
    iterator = iter(string_collection)
    while True:
        try:
            current_element = next(iterator)
        except StopIteration:
            break
        if not current_element.startswith(prefix_value):
            continue
        result_collection.append(current_element)
    return result_collection