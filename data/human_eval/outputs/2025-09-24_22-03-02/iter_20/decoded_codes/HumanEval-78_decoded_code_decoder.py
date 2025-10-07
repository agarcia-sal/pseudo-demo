from typing import Union

def hex_key(num: Union[str, list[str]]) -> int:
    primes = ['2', '3', '5', '7', 'B', 'D']
    total = 0
    for i in range(len(num)):
        if num[i] in primes:
            total += 1
    return total