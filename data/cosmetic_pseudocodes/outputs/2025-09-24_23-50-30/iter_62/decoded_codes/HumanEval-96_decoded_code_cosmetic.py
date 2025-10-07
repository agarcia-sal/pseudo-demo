from typing import List

def count_up_to(a: int) -> List[int]:
    def check_prime(x: int, y: int) -> bool:
        if y * y > x:
            return True
        elif x % y == 0:
            return False
        else:
            return check_prime(x, y + 1)

    def build_primes(z: int, acc: List[int]) -> List[int]:
        if z >= a:
            return acc
        elif check_prime(z, 2):
            return build_primes(z + 1, acc + [z])
        else:
            return build_primes(z + 1, acc)

    return build_primes(2, [])