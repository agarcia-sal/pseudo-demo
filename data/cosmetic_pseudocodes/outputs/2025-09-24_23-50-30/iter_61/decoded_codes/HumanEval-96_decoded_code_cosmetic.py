from typing import List


def count_up_to(alpha: int) -> List[int]:
    primesList: List[int] = []

    def check_division(beta: int, gamma: int, delta: int) -> bool:
        if beta % gamma == 0:
            return False
        if gamma + 1 < delta:
            return check_division(beta, gamma + 1, delta)
        return True

    def iterate_candidates(epsilon: int, zeta: int, results: List[int]) -> List[int]:
        if epsilon >= zeta:
            return results
        primeFlag = check_division(epsilon, 2, epsilon)
        updatedResults = results + [epsilon] if primeFlag else results
        return iterate_candidates(epsilon + 1, zeta, updatedResults)

    return iterate_candidates(2, alpha, primesList)