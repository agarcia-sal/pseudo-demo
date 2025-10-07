from typing import List, TypeVar

T = TypeVar('T')

def strange_sort_list(collection: List[T]) -> List[T]:
    output: List[T] = []
    toggle = False
    collection = collection[:]  # copy to avoid mutating input
    while collection:
        toggle = not toggle
        if toggle:
            chosen_value = min(collection)
        else:
            chosen_value = max(collection)
        output.append(chosen_value)
        collection.remove(chosen_value)
    return output