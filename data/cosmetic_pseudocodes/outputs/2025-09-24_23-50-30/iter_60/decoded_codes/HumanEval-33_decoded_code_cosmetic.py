from typing import List

def sort_third(alpha: List[int]) -> List[int]:

    def replace_at_indices(
        beta: List[int], gamma: int, delta: int, epsilon: List[int], zeta: int
    ) -> List[int]:
        if zeta == len(beta):
            return beta
        if (zeta % 3) == 0:
            beta[zeta] = epsilon[delta]
            return replace_at_indices(beta, gamma, delta + 1, epsilon, zeta + 1)
        return replace_at_indices(beta, gamma, delta, epsilon, zeta + 1)

    def extract_indices(
        theta: List[int], i: int, acc: List[int]
    ) -> List[int]:
        if i == len(theta):
            return acc
        if (i % 3) == 0:
            return extract_indices(theta, i + 1, acc + [theta[i]])
        return extract_indices(theta, i + 1, acc)

    omega: List[int] = []
    omega = extract_indices(alpha, 0, omega)
    beta = omega
    gamma = len(beta)

    def insertion_sort(arr: List[int], n: int) -> List[int]:
        for m in range(1, n):
            key = arr[m]
            p = m - 1
            while p >= 0 and arr[p] > key:
                arr[p + 1] = arr[p]
                p -= 1
            arr[p + 1] = key
        return arr

    sorted_beta = insertion_sort(beta, gamma)
    return replace_at_indices(alpha, beta, 0, sorted_beta, 0)