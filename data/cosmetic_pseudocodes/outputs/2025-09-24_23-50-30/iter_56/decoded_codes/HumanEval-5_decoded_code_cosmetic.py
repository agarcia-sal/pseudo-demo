from typing import TypeVar, Sequence, List

T = TypeVar('T')
U = TypeVar('U')

def intersperse(collection_alpha: Sequence[T], separator_beta: U) -> List[T | U]:
    if len(collection_alpha) == 0:
        return []
    accumulator_theta: List[T | U] = []
    index_mu = 0
    while index_mu < len(collection_alpha) - 1:
        accumulator_theta.append(collection_alpha[index_mu])
        accumulator_theta.append(separator_beta)
        index_mu += 1
    accumulator_theta.append(collection_alpha[-1])
    return accumulator_theta