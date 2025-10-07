from typing import Iterable, List, Union

def filter_integers(values: Iterable[Union[int, object]]) -> List[int]:
    return [x for x in values if isinstance(x, int)]