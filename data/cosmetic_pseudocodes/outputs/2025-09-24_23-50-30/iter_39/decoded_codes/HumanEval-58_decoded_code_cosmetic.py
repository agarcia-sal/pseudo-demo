from typing import List, Set, TypeVar, Iterable

T = TypeVar('T', bound=object)

def common(alpha: Iterable[T], beta: Iterable[T]) -> List[T]:
    gamma: Set[T] = set()

    def traverse_omega(delta: Iterable[T], epsilon: Iterable[T]) -> None:
        delta_iter = iter(delta)
        try:
            first_delta = next(delta_iter)
        except StopIteration:
            return

        def traverse_theta(zeta: Iterable[T]) -> None:
            zeta_iter = iter(zeta)
            try:
                first_zeta = next(zeta_iter)
            except StopIteration:
                return

            if first_delta == first_zeta:
                gamma.add(first_delta)
            traverse_theta(zeta_iter)

        traverse_theta(epsilon)
        traverse_omega(delta_iter, epsilon)

    traverse_omega(alpha, beta)
    return sorted(gamma)