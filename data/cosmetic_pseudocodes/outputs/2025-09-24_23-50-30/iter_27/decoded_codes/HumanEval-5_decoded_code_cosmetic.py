from typing import TypeVar, Sequence, List

T = TypeVar('T')
U = TypeVar('U')

def intersperse(sequence_alpha: Sequence[T], separator_beta: U) -> List[object]:
    if not sequence_alpha:
        return []
    collection_gamma: List[object] = []
    index_delta = 0
    while index_delta < len(sequence_alpha) - 1:
        collection_gamma.append(sequence_alpha[index_delta])
        collection_gamma.append(separator_beta)
        index_delta += 1
    collection_gamma.append(sequence_alpha[-1])
    return collection_gamma