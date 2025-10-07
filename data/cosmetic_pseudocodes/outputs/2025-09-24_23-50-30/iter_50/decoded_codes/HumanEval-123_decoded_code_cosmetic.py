from typing import List


def get_odd_collatz(alpha: int) -> List[int]:
    def collatz_iter(beta: List[int], gamma: int) -> int:
        if gamma <= 1:
            return gamma
        if gamma % 2 == 0:
            gamma //= 2
            return collatz_iter(beta, gamma)
        else:  # gamma % 2 == 1
            gamma = gamma * 3 + 1
            beta.append(gamma)
            return collatz_iter(beta, gamma)

    def sort_list(delta: List[int]) -> List[int]:
        return sorted(delta)

    gamma_list: List[int] = []
    if alpha % 2 == 1:
        gamma_list = [alpha]

    while alpha > 1:
        if alpha % 2 == 0:
            alpha //= 2
        else:
            alpha = alpha * 3 + 1
        if alpha % 2 == 1:
            gamma_list.append(alpha)

    return sort_list(gamma_list)