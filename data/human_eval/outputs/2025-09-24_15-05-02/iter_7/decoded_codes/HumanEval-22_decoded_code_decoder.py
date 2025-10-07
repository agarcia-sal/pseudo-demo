from typing import Iterable, List, Union

def filter_integers(values: Iterable) -> List[int]:
    return [x for x in values if isinstance(x, int)]