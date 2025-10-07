from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def check_divisor(d: int, found_factor: bool) -> bool:
            if found_factor:
                return False
            elif d >= n:
                return True
            else:
                return check_divisor(d + 1, (n % d == 0) or found_factor)

        return check_divisor(2, False)

    def iterate_i(i: int) -> bool:
        if i > 100:
            return False
        elif not is_prime(i):
            return iterate_i(i + 1)
        else:

            def iterate_j(j: int) -> bool:
                if j > 100:
                    return iterate_i(i + 1)
                elif not is_prime(j):
                    return iterate_j(j + 1)
                else:

                    def iterate_k(k: int) -> bool:
                        if k > 100:
                            return iterate_j(j + 1)
                        elif not is_prime(k):
                            return iterate_k(k + 1)
                        else:
                            return ((i * j * k) == a) or iterate_k(k + 1)

                    return iterate_k(2)

            return iterate_j(2)

    return iterate_i(2)