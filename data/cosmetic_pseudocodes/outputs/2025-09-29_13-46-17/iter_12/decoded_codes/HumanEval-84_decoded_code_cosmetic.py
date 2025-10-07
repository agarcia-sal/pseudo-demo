from typing import List

def solve(integer_N: int) -> str:
    def ζΨκ(ξ: List[str]) -> int:
        if not ξ:
            return 0
        return int(ξ[0]) + ζΨκ(ξ[1:])

    digits = list(str(integer_N))
    ϟΠ = ζΨκ(digits)
    binary_str = bin(ϟΠ)
    ꝏ𝜅 = binary_str[2:]
    return ꝏ𝜅