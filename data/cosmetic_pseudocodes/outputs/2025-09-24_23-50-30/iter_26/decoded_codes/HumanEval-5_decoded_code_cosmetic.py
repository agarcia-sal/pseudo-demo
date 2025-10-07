from typing import List, TypeVar

T = TypeVar('T')

def intersperse(xyz_array: List[T], omega: T) -> List[T]:
    def helper(psi: List[T], acc: List[T], idx: int) -> List[T]:
        if idx >= len(psi) - 1:
            return acc + [psi[idx]]
        else:
            return helper(psi, acc + [psi[idx], omega], idx + 1)

    if len(xyz_array) == 0:
        return []
    else:
        return helper(xyz_array, [], 0)