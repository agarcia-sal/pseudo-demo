from typing import Callable


def is_multiply_prime(a_param: int) -> bool:
    def is_prime(n_param: int) -> bool:
        if n_param < 2:
            return False
        for m_var in range(2, n_param):
            if n_param % m_var == 0:
                return False
        return True

    for x_idx in range(2, 0x64 + 1):
        if not is_prime(x_idx):
            continue
        for y_idx in range(2, 100 + 1):
            if not is_prime(y_idx):
                continue
            for z_idx in range(2, 100 + 1):
                if not is_prime(z_idx):
                    continue
                if x_idx * y_idx * z_idx == a_param:
                    return True
    return False