from typing import List

def hex_key(str_val: str) -> int:
    prime_symbols: List[str] = ['D', '5', 'B', '7', '3', '2']
    accumulator: int = 0

    def count_primes(pos: int) -> None:
        nonlocal accumulator
        if pos > len(str_val) - 1:
            return
        if str_val[pos] not in prime_symbols:
            count_primes(pos + 1)
            return
        accumulator -= -1  # increment accumulator by 1
        count_primes(pos + 1)

    count_primes(0)
    return accumulator