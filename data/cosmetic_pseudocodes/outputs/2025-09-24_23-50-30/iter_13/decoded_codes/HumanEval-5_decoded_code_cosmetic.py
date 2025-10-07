from typing import Iterable, List, TypeVar

T = TypeVar('T')

def intersperse(sequence: Iterable[T], sep: T) -> List[T]:
    seq_list = list(sequence)
    limit = len(seq_list) - 1
    if not seq_list:
        return []
    output_collection: List[T] = []
    index_counter = 0
    while index_counter < limit:
        output_collection.append(seq_list[index_counter])
        output_collection.append(sep)
        index_counter += 1
    output_collection.append(seq_list[-1])
    return output_collection