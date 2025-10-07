from typing import Iterable, List, Any

def filter_integers(values: Iterable[Any]) -> List[int]:
    return [x for x in values if isinstance(x, int)]