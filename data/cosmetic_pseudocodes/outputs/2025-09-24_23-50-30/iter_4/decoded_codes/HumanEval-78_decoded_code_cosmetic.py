from typing import Literal

def hex_key(string_num: str) -> int:
    primes_collection: str = '2357BD'

    def count_primes(pos: int, count: int) -> int:
        if pos == len(string_num):
            return count
        return count_primes(pos + 1, count + (1 if string_num[pos] in primes_collection else 0))

    return count_primes(0, 0)