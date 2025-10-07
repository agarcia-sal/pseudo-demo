from typing import List


def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        p: int = 2
        while p * p <= x:
            if x % p == 0:
                return False
            p += 1
        return True

    primes_collection: List[int] = [val for val in range(2, 101) if is_prime(val)]

    for first_element in primes_collection:
        for second_element in primes_collection:
            # If product of first and second elements exceeds a, skip inner loop early to reduce operations
            product_two = first_element * second_element
            if product_two > a or a % product_two != 0:
                continue
            for third_element in primes_collection:
                if product_two * third_element == a:
                    return True
    return False