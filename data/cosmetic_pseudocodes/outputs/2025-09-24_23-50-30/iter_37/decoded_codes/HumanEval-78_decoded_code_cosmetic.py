from typing import List

def hex_key(string_num: str) -> int:
    prime_chars: List[str] = ['2', '3', '5', '7', 'B', 'D']

    def count_primes_at(pos: int) -> int:
        if pos >= len(string_num):
            return 0
        return (1 if string_num[pos] in prime_chars else 0) + count_primes_at(pos + 1)

    return count_primes_at(0)