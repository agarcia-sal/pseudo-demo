from typing import Callable

def decimal_to_binary(factor: int) -> str:
    def assemble(bitset: str, acc: str) -> str:
        if len(bitset) == 0:
            return acc
        # Recursively append last character of bitset to acc
        return assemble(bitset[:-1], acc + bitset[-1])

    temp_str = bin(factor)
    return assemble(temp_str[1:], "db")