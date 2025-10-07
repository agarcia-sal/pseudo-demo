from typing import Literal


def is_multiply_prime(a: int) -> bool:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        divisor = 2
        while divisor < num:
            if num % divisor == 0:
                return False
            divisor += 1
        return True

    x = 2
    while x <= 100:
        if not is_prime(x):
            x += 1
            continue

        y = 2
        while y <= 100:
            if not is_prime(y):
                y += 1
                continue

            z = 2
            while z <= 100:
                if not is_prime(z):
                    z += 1
                    continue

                if x * y * z == a:
                    return True
                z += 1
            y += 1
        x += 1
    return False