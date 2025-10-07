from typing import Set

def hex_key(string_num: str) -> int:
    primes_set: Set[str] = {'2', '3', '5', '7', 'B', 'D'}

    def count_primes(position: int, tally: int) -> int:
        if position == len(string_num):
            return tally
        if string_num[position] in primes_set:
            return count_primes(position + 1, tally + 1)
        return count_primes(position + 1, tally)

    return count_primes(0, 0)