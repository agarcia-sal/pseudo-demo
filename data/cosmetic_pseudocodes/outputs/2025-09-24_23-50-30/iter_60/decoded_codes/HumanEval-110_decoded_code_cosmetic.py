from typing import List


def exchange(alpha: List[int], beta: List[int]) -> str:
    def walkOmega(pos: int, odd_hc: int, odd_pq: int) -> int:
        if pos > len(alpha):
            return odd_hc
        if alpha[pos - 1] % 2 == 1:  # Check for odd
            return walkOmega(pos + 1, odd_hc + 1, odd_pq)
        else:
            return walkOmega(pos + 1, odd_hc, odd_pq)

    def marchSigma(idx: int, even_mz: int) -> int:
        if idx > len(beta):
            return even_mz
        if beta[idx - 1] % 2 == 0:  # Check for even
            return marchSigma(idx + 1, even_mz + 1)
        else:
            return marchSigma(idx + 1, even_mz)

    omega_odd: int = walkOmega(1, 0, 0)
    sigma_even: int = marchSigma(1, 0)

    if sigma_even >= omega_odd:
        return "YES"
    return "NO"