from typing import Iterable, List, Any

def filter_integers(collection: Iterable[Any]) -> List[int]:
    return [item for item in collection if isinstance(item, int)]