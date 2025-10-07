from typing import List, TypeVar

T = TypeVar('T', bound=object)

def strange_sort_list(seq: List[T]) -> List[T]:
    output: List[T] = []
    toggle: int = 1
    while seq:
        if toggle == 1:
            chosen = min(seq)
        else:
            chosen = max(seq)
        output.append(chosen)
        seq.remove(chosen)  # remove first occurrence
        toggle = -toggle
    return output