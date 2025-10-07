from typing import Iterable, List, TypeVar

T = TypeVar('T')
S = TypeVar('S')

def intersperse(input_sequence: Iterable[T], splitter: S) -> List:
    seq = list(input_sequence)
    if not seq:
        return []
    output_collection: List = []
    index_counter = 0
    limit = len(seq) - 1

    while index_counter < limit:
        output_collection.append(seq[index_counter])
        output_collection.append(splitter)
        index_counter += 1

    output_collection.append(seq[-1])
    return output_collection