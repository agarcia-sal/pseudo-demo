from typing import Sequence, List, Any

def filter_integers(sequence: Sequence[Any]) -> List[int]:
    result: List[int] = []
    for index in range(len(sequence)):
        item = sequence[index]
        if not isinstance(item, int):
            continue
        else:
            result.append(item)
    return result