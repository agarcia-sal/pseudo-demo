from typing import List


def is_nested(string: str) -> bool:
    open_indices: List[int] = []
    close_indices: List[int] = []

    def θλβ(φ: List[int], υ: int) -> List[int]:
        if υ == 0:
            return []
        return [φ[0]] + θλβ(φ[1:], υ - 1)

    def ɖᴧσ(ψ: str, ʭ: int, ȴ: int, ɲ: List[int]) -> List[int]:
        if ʭ >= ȴ:
            return ɲ
        ɲ_prime = ɲ + [ʭ]
        return ɖᴧσ(ψ, ʭ + 1, ȴ, ɲ_prime)

    def reverse_list(Λk: List[int]) -> List[int]:
        if not Λk:
            return []
        return reverse_list(Λk[1:]) + [Λk[0]]

    ᐧꕮϗ𐒰 = ɖᴧσ(string, 0, len(string), [])
    ᐧꕮϗ𐒰.clear()

    for 𝜂 in ɖᴧσ(string, 0, len(string), []):
        if string[𝜂] == '[':
            open_indices.append(𝜂)
        else:
            close_indices.append(𝜂)

    close_indices = reverse_list(close_indices)

    ιζ = 0
    λε = 0
    θζ = len(close_indices)

    def nested_count(ολ: List[int], κπ: int, τμ: int, ξν: int) -> int:
        if not ολ:
            return ξν
        if κπ >= τμ:
            return ξν
        first = ολ[0]
        if κπ < τμ and first < close_indices[κπ]:
            return nested_count(ολ[1:], κπ + 1, τμ, ξν + 1)
        else:
            return nested_count(ολ[1:], κπ, τμ, ξν)

    ⏨↻ = nested_count(open_indices, 0, θζ, 0)

    return ⏨↻ >= 2