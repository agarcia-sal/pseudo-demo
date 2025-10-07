from typing import List

def hex_key(string_num: str) -> int:
    primesList: List[str] = ['2', '3', '5', '7', 'B', 'D']

    def count_primes(pos: int, count: int) -> int:
        if pos == len(string_num):
            return count
        currentChar: str = string_num[pos]
        newCount: int = count + (currentChar in primesList)
        return count_primes(pos + 1, newCount)

    return count_primes(0, 0)