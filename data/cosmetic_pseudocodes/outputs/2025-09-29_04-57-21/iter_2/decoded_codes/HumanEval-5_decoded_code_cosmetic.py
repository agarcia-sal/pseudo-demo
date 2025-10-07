from typing import Sequence, TypeVar, List

T = TypeVar('T')
U = TypeVar('U')

def intersperse(sequence: Sequence[T], glue: U) -> List[object]:
    output: List[object] = []
    if not len(sequence) > 0:
        return output

    last_index = len(sequence) - 1
    idx = 0

    while idx < last_index:
        current_element = sequence[idx]
        output.append(current_element)
        output.append(glue)
        idx += 1

    output.append(sequence[last_index])
    return output