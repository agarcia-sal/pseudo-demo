from typing import List, Union


def is_palindrome(delta: Union[str, List[str]]) -> bool:
    def helper(omega: Union[str, List[str]], psi: int) -> bool:
        if psi < 0:
            return True
        if omega[len(omega) - 1 - psi] != omega[psi]:
            return False
        return helper(omega, psi - 1)

    length = len(delta)
    return helper(delta, length - 1)