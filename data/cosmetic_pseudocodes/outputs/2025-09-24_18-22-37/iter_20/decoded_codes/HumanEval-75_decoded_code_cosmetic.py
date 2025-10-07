from typing import Optional


def is_multiply_prime(beta: int) -> bool:
    def is_prime(omega: int) -> bool:
        if omega < 2:
            return False
        idx: int = 2
        while idx < omega:
            if omega % idx == 0:
                return False
            idx += 1
        return True

    x_val: int = 2
    while x_val <= 0x64:  # 100 decimal
        if not is_prime(x_val):
            x_val += 1
            continue

        y_val: int = 2
        while y_val <= 100:
            if not is_prime(y_val):
                y_val += 1
                continue

            z_val: int = 2
            while z_val <= 100:
                if not is_prime(z_val):
                    z_val += 1
                    continue

                if x_val * y_val * z_val == beta:
                    return True
                z_val += 1

            y_val += 1

        x_val += 1

    return False