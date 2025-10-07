from typing import Iterable, List, Union


def filter_integers(input_collection: Iterable[object]) -> List[int]:
    return [item for item in input_collection if isinstance(item, int)]