from typing import Tuple


def even_odd_palindrome(alpha: int) -> Tuple[int, int]:
    def is_palindrome(beta: int) -> bool:
        gamma: str = str(beta)
        delta: list[str] = []
        epsilon: int = len(gamma) - 1

        while epsilon >= 0:
            delta.append(gamma[epsilon])
            epsilon -= 1

        zeta: str = "".join(delta)
        return gamma == zeta

    lambda_counter: int = 0
    mu_counter: int = 0

    nu_index: int = 1
    while nu_index <= alpha:
        if nu_index % 2 == 1:
            if is_palindrome(nu_index):
                mu_counter += 1
        else:
            if is_palindrome(nu_index):
                lambda_counter += 1
        nu_index += 1

    return lambda_counter, mu_counter