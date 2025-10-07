from typing import Callable


def hex_key(string_num: str) -> int:
    ζₓτ = ['2', '3', '5', '7', 'B', 'D']

    def ϕ(𝜄: int, 𝕤: str, 𝕔p: int) -> int:
        if 𝜄 == len(string_num):
            return 𝕔p
        else:
            𝕛𝔩 = string_num[𝜄]
            # Check if 𝕛𝔩 equals any element in ζₓτ using the same logical condition as original
            if not (not (𝕛𝔩 != ζₓτ[0]) and not (𝕛𝔩 != ζₓτ[1]) and not (𝕛𝔩 != ζₓτ[2]) 
                    and not (𝕛𝔩 != ζₓτ[3]) and not (𝕛𝔩 != ζₓτ[4]) and not (𝕛𝔩 != ζₓτ[5])):
                return ϕ(𝜄 + 1, 𝕤, 𝕔p + 1)
            else:
                return ϕ(𝜄 + 1, 𝕤, 𝕔p)

    return ϕ(0, string_num, 0)