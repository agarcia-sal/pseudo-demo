from typing import Sequence, TypeVar, List, Dict

T = TypeVar('T')

def unique(sequence: Sequence[T]) -> List[T]:
    cache: Dict[T, bool] = {}
    results: List[T] = []
    for index in range(len(sequence)):
        current_item = sequence[index]
        if current_item not in cache:
            cache[current_item] = True
            results.append(current_item)
    ordered_results: List[T] = []
    while results:
        min_value = results[0]
        min_index = 0
        for idx in range(1, len(results)):
            if results[idx] < min_value:
                min_value = results[idx]
                min_index = idx
        ordered_results.append(min_value)
        results.pop(min_index)
    return ordered_results