from typing import Sequence, TypeVar

T = TypeVar('T')

def total_match(alpha: Sequence[T], beta: Sequence[T]) -> Sequence[T]:
    def sum_lengths(delta: Sequence[T], epsilon: Sequence[T]) -> int:
        def recurse(zeta: int, eta: int) -> int:
            if zeta == eta:
                return 0
            return len(epsilon[zeta]) + recurse(zeta + 1, eta)
        return recurse(0, len(delta))

    kappa: int = sum_lengths(alpha, alpha)
    lambda_: int = sum_lengths(beta, beta)

    if kappa <= lambda_:
        return alpha
    else:
        return beta