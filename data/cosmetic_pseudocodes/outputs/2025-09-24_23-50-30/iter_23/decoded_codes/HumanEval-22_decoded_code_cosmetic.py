from typing import Iterable, List, Union

def filter_integers(sequence_container: Iterable[object]) -> List[int]:
    return [each_item for each_item in sequence_container if isinstance(each_item, int)]