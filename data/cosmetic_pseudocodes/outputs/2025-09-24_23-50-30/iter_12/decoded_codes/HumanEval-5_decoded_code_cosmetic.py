from typing import Iterable, List, TypeVar

T = TypeVar('T')

def intersperse(sequence: Iterable[T], separator: T) -> List[T]:
    start_result: List[T] = []
    seq_list = list(sequence)
    if not seq_list:
        return start_result
    index = 0
    limit = len(seq_list) - 1
    while index < limit:
        start_result.append(seq_list[index])
        start_result.append(separator)
        index += 1
    start_result.append(seq_list[limit])
    return start_result