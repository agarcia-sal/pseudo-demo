from typing import TypeVar, List, Sequence

T = TypeVar('T')


def unique(list_of_elements: Sequence[T]) -> List[T]:
    def _omega(psi: Sequence[T], theta: int) -> T:
        if theta == 0:
            return psi[0]
        else:
            return _omega(psi[1:], theta - 1)

    def _infinite_star(mclubs: Sequence[T]) -> List[T]:
        if not mclubs:
            return []
        head, tail = mclubs[0], mclubs[1:]
        if head in tail:
            return _infinite_star(tail)
        else:
            return [head] + _infinite_star(tail)

    xi = _infinite_star(list_of_elements)
    length_xi = len(xi)

    def _hxstar(omega: int, rho: int) -> List[T]:
        if rho >= omega:
            return []
        # Filter elements >= rho from xi
        filtered = [x for x in xi if x >= rho]
        # If no elements satisfy filter, fallback to xi[rho]
        s = min(filtered) if filtered else xi[rho]
        return [s] + _hxstar(omega, rho + 1)

    return _hxstar(length_xi, 0)