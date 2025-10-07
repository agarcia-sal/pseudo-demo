from typing import List


def separate_paren_groups(alpha: str) -> List[str]:
    omega: List[str] = []
    sigma: List[str] = []
    delta: int = 0

    def unwind(index: int) -> None:
        nonlocal delta
        if index >= len(alpha):
            return
        epsilon = alpha[index]
        if epsilon == '(':
            delta += 1
            sigma.append(epsilon)
        elif epsilon == ')':
            delta -= 1
            sigma.append(epsilon)
            if delta == 0:
                omega.append("".join(sigma))
                sigma.clear()
        # else: no operation
        unwind(index + 1)

    unwind(0)
    return omega