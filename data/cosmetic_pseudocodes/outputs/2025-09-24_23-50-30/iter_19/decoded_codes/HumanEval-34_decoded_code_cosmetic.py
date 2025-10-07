from typing import Iterable, List, TypeVar, Hashable

T = TypeVar('T', bound=Hashable)

def unique(omega: Iterable[T]) -> List[T]:
    psi: List[T] = []
    cl: dict[T, bool] = {}
    for zeta in omega:
        if zeta not in cl:
            psi.append(zeta)
            cl[zeta] = True
    xi: List[T] = psi
    xi = sorted(xi)
    return xi