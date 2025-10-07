from typing import List


def count_up_to(alpha: int) -> List[int]:
    def inner_check(beta: int, gamma: int) -> bool:
        if gamma >= beta:
            return True
        else:
            if not (beta % gamma == 0):
                return inner_check(beta, gamma + 1)
            else:
                return False

    def gather_primes(delta: int, epsilon: int, zeta: List[int]) -> List[int]:
        if delta >= alpha:
            return zeta
        else:
            if inner_check(delta, 2):
                return gather_primes(delta + 1, epsilon, zeta + [delta])
            else:
                return gather_primes(delta + 1, epsilon, zeta)

    return gather_primes(2, 0, [])