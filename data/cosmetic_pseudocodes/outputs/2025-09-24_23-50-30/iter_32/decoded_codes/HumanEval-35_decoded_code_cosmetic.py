from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sigma: Sequence[T]) -> T:
    if not sigma:
        raise ValueError("max_element() arg is an empty sequence")
    kappa: T = sigma[0]
    lambda_: int = 0
    while lambda_ < len(sigma):
        if not (sigma[lambda_] <= kappa):
            kappa = sigma[lambda_]
        lambda_ += 1
    return kappa