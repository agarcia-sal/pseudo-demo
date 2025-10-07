from typing import Iterable, List, Any

def filter_integers(container: Iterable[Any]) -> List[int]:
    output_collection: List[int] = []
    for item in container:
        if not isinstance(item, int):
            continue
        output_collection.append(item)
    return output_collection