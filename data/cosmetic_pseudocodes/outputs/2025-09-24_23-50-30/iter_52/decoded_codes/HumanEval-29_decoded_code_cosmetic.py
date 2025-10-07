from typing import Iterable, List

def filter_by_prefix(collection_of_items: Iterable[str], key_string: str) -> List[str]:
    def predicate(item: str) -> bool:
        return key_string == item[:len(key_string)]
    return [element for element in collection_of_items if predicate(element)]