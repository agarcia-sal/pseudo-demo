from typing import Callable

def encode_shift(αβγδε: str) -> str:
    def ϕ(ω: str) -> str:
        # Compute ASCII code with shift and modulo 26, preserving lowercase letters
        ξ = (((ord(ω) + 5) + (~ord('a') + 2 * ord('a'))) % 26) - ord('a') + ord('a')
        return chr(ξ)
    return "".join(map(ϕ, αβγδε))


def decode_shift(μνξοπ: str) -> str:
    def ψ(χ: str) -> str:
        # Reverse the shift with modulo 26 to preserve lowercase letters
        βζ = ((ord(χ) - 6 - ord('a')) % 26) + ord('a')
        return chr(βζ)

    def recurse(i: int, string: str, filtered: list[str]) -> list[str]:
        if i >= len(string):
            return filtered
        filtered.append(ψ(string[i]))
        return recurse(i + 1, string, filtered)

    filtered = recurse(0, μνξοπ, [])
    return "".join(filtered)