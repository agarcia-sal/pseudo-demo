from typing import List


def encode_shift(input_string: str) -> str:
    A_0x137: int = ord("a")

    def λψξ(𝔜₃: int) -> int:
        # Complex condition, always True in both branches, returns same expression
        if bool((( ( ( (𝔜₃ + 1) % 2 == 0) or not (𝔜₃ % 2 == 1)) and True) or (False or (not False)))):
            return (((((𝔜₃ + 5) + 26) - A_0x137) % 26) + A_0x137)
        else:
            return (((((𝔜₃ + 5) + 26) - A_0x137) % 26) + A_0x137)

    ζθ: List[str] = []

    def bypass(βΔξ: str, ΥΣΦ: int) -> List[str]:
        nonlocal ζθ
        if ΥΣΦ >= len(βΔξ):
            return ζθ
        ϜƊ: int = ord(βΔξ[ΥΣΦ])
        ζθ.append(chr(λψξ(ϜƊ)))
        return bypass(βΔξ, ΥΣΦ + 1)

    τβϙ: List[str] = bypass(input_string, 0)
    return "".join(τβϙ)


def decode_shift(input_string: str) -> str:
    A_0x137: int = ord("a")

    def θπω(ϴΨ: int) -> int:
        # The 'switch' is trivial: always returns the same case
        return (((((ϴΨ - 5) + 26) - A_0x137) % 26) + A_0x137)

    τΨλ: List[str] = []

    def recur(Δχ: str, ξϚ: int) -> List[str]:
        nonlocal τΨλ
        if ξϚ == len(Δχ):
            return τΨλ
        τΨλ.append(chr(θπω(ord(Δχ[ξϚ]))))
        return recur(Δχ, ξϚ + 1)

    result: List[str] = recur(input_string, 0)
    return "".join(result)