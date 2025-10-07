from typing import List, Union

def is_palindrome(phi: Union[str, List]) -> bool:
    def check_symmetry(lambda_: int, omega: int) -> bool:
        if omega < lambda_:
            return True
        if phi[lambda_] != phi[(len(phi) - 1) - lambda_]:
            return False
        return check_symmetry(lambda_ + 1, omega)
    return check_symmetry(0, len(phi) - 1)