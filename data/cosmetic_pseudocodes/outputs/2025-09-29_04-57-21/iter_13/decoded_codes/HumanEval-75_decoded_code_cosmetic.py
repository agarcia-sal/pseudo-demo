from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for divisor in range(2, n):
            if n % divisor == 0:
                return False
        return True

    current_i: int = 0  # will be assigned during scan_i

    def scan_k(k_val: int, j_val: int) -> bool:
        nonlocal current_i
        if k_val > 100:
            return False
        if not is_prime(k_val):
            return scan_k(k_val + 1, j_val)
        if a == j_val * k_val * current_i:
            return True
        return scan_k(k_val + 1, j_val)

    def scan_j(j_val: int) -> bool:
        if j_val > 100:
            return False
        if not is_prime(j_val):
            return scan_j(j_val + 1)
        return scan_k(2, j_val)

    def scan_i(i_val: int) -> bool:
        nonlocal current_i
        if i_val > 100:
            return False
        if not is_prime(i_val):
            return scan_i(i_val + 1)
        current_i = i_val
        if scan_j(2):
            return True
        return scan_i(i_val + 1)

    return scan_i(2)