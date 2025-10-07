from typing import Generator


def digits(n: int) -> Generator[int, None, None]:
    # Generate digits of n in order from most significant to least significant
    if n == 0:
        yield 0
        return
    # Determine highest power of 10 <= n
    power = 1
    while power <= n // 10:
        power *= 10
    while power > 0:
        digit = n // power
        yield digit
        n %= power
        power //= 10