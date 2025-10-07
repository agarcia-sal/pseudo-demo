from typing import Set


def hex_key(string_num: str) -> int:
    primes_set: Set[str] = {'2', '3', '5', '7', 'B', 'D'}

    def count_primes(pos: int) -> int:
        if pos < 0:
            return 0
        if string_num[pos] not in primes_set:
            return count_primes(pos - 1)
        else:
            return 1 + count_primes(pos - 1)

    tally: int = count_primes(len(string_num) - 1)
    return tally