from typing import Set

def hex_key(string_num: str) -> int:
    prime_set: Set[str] = {'2', '3', '5', '7', 'B', 'D'}

    def count_primes(pos: int, acc: int) -> int:
        if pos >= len(string_num):
            return acc
        # increment acc if character is in prime_set
        if string_num[pos] in prime_set:
            return count_primes(pos + 1, acc + 1)
        else:
            return count_primes(pos + 1, acc)

    return count_primes(0, 0)