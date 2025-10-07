from typing import Sequence, List, TypeVar

T = TypeVar('T')

def all_prefixes(parameter_one: Sequence[T]) -> List[Sequence[T]]:
    accumulator: List[Sequence[T]] = []
    counter: int = 0
    while counter < len(parameter_one):
        partial = parameter_one[0 : counter + 1]
        accumulator.append(partial)
        counter += 1
    return accumulator