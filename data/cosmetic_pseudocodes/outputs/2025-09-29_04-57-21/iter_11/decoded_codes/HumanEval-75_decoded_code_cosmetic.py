from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        test_divisor = 2
        while test_divisor < n:
            if n % test_divisor == 0:
                return False
            test_divisor += 1
        return True

    prime_candidate_x = 2
    while prime_candidate_x <= 100:
        if not is_prime(prime_candidate_x):
            prime_candidate_x += 1
            continue

        prime_candidate_y = 2
        while prime_candidate_y <= 100:
            if not is_prime(prime_candidate_y):
                prime_candidate_y += 1
                continue

            prime_candidate_z = 2
            while prime_candidate_z <= 100:
                if not is_prime(prime_candidate_z):
                    prime_candidate_z += 1
                    continue

                if prime_candidate_x * prime_candidate_y * prime_candidate_z == a:
                    return True

                prime_candidate_z += 1

            prime_candidate_y += 1

        prime_candidate_x += 1

    return False