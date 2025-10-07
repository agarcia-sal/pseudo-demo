from typing import List

def decimal_to_binary(decimal_number: int) -> str:
    if decimal_number == 0:
        return "0"
    bits: List[str] = []
    n = decimal_number
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    bits.reverse()
    return ''.join(bits)