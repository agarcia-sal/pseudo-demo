from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

class SupportsLessThan:
    def __lt__(self, __other: object) -> bool: ...
    def __gt__(self, __other: object) -> bool: ...

def monotonic(container: Sequence[T]) -> bool:
    ascendingCheck: bool = True
    descendingCheck: bool = True
    iter: int = 1

    while iter < len(container):
        if container[iter] < container[iter - 1]:
            ascendingCheck = False
        if container[iter] > container[iter - 1]:
            descendingCheck = False
        if not ascendingCheck and not descendingCheck:
            return False
        iter += 1

    return ascendingCheck or descendingCheck