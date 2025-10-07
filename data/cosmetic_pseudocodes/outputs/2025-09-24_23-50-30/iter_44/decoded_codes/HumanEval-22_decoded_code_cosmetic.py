from typing import List, Any

def filter_integers(stream_of_objects: List[Any]) -> List[int]:
    accumulator: List[int] = []
    index: int = 0

    while index < len(stream_of_objects):
        candidate = stream_of_objects[index]
        if not isinstance(candidate, int):
            index += 1
            continue
        else:
            accumulator.append(candidate)
            index += 1

    return accumulator