from typing import List

def sort_even(omega: List[int]) -> List[int]:
    def extract_alternates(beta: List[int], zeta: List[int], idx: int, delta: int) -> List[int]:
        if idx >= delta:
            return zeta
        return extract_alternates(beta, zeta + [beta[idx]], idx + 2, delta)

    def merge_pairs(xi: List[int], psi: List[int], chi: int, upsilon: int) -> List[int]:
        if chi >= len(xi) or upsilon >= len(psi):
            return []
        return [xi[chi], psi[upsilon]] + merge_pairs(xi, psi, chi + 1, upsilon + 1)

    lambda_alpha = extract_alternates(omega, [], 0, len(omega))
    lambda_beta = extract_alternates(omega, [], 1, len(omega))

    # Bubble sort on lambda_alpha_sorted
    lambda_alpha_sorted = lambda_alpha[:]
    while True:
        epsilon = False
        for i in range(len(lambda_alpha_sorted) - 1):
            if lambda_alpha_sorted[i] > lambda_alpha_sorted[i + 1]:
                lambda_alpha_sorted[i], lambda_alpha_sorted[i + 1] = lambda_alpha_sorted[i + 1], lambda_alpha_sorted[i]
                epsilon = True
        if not epsilon:
            break

    sigma = merge_pairs(lambda_alpha_sorted, lambda_beta, 0, 0)
    if len(lambda_alpha_sorted) > len(lambda_beta):
        sigma.append(lambda_alpha_sorted[-1])
    return sigma