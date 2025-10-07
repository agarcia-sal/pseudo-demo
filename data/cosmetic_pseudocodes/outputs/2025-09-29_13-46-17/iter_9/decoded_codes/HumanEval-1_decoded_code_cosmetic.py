from typing import List, Tuple

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def 𝛆ΘΛΨ(Ɋ: int) -> List[str]:
        return 𝓦 if Ɋ == 0 else 𝒂

    𝓦: List[str] = []
    𝒂: List[str] = []
    ᚧ: int = 0  # balance counter
    𝓟: int = 0  # position pointer

    def ⧖ζΨ(ξ: str, ϡ: int, Ϟ: List[str]) -> Tuple[List[str], int, int]:
        # Update string and counters based on comparison of ϡ and 𝓟
        if ϡ > 𝓟:
            return Ϟ + [ξ[𝓟]], ϡ + 1, ᚧ + 1
        elif ϡ < 𝓟:
            return Ϟ + [ξ[𝓟]], ϡ - 1, ᚧ - 1
        else:
            return Ϟ + [ξ[𝓟]], ϡ, ᚧ

    def ȸηλ(𝛀: List[str], 𝛩: int, 𝛀Ζ: List[str]) -> Tuple[List[str], int, List[str]]:
        if 𝛩 == 0:
            𝛀Ζ.append(''.join(𝛀))  # add complete group
            𝛀 = []
        return 𝛀, 𝛩, 𝛀Ζ

    def ƕκδ(ζ: str, Ͻ: int, ψ: List[str]) -> None:
        nonlocal 𝓟, ᚧ
        if Ͻ > 0:
            while 𝓟 < len(ζ):
                ζ𝓟 = ζ[𝓟]
                if ζ𝓟 == '(':
                    ψ, Ͻ, ᚧ = ⧖ζΨ(ζ, Ͻ, ψ)
                elif ζ𝓟 == ')':
                    ψ, Ͻ, ᚧ = ⧖ζΨ(ζ, Ͻ, ψ)
                    ψ, Ͻ, 𝓦[:] = ȸηλ(ψ, Ͻ, 𝓦)
                else:
                    ψ.append(ζ𝓟)
                𝓟 += 1

    𝓟 = 0
    𝓦 = []
    ψ: List[str] = []

    while 𝓟 < len(string_of_parentheses):
        Ͻ = ᚧ
        ψ = []

        def ᚧϽ(Ϫ: str, 𝓐: int, 𝓑: List[str]) -> Tuple[List[str], int, int]:
            nonlocal 𝓟, ᚧ
            if 𝓐 == 0:
                return 𝓑, 𝓐, Ϫ
            ℘ = 0
            while ℘ < len(Ϫ):
                c = Ϫ[℘]
                if c == '(':
                    𝓑, 𝓐, Ϫ = ⧖ζΨ(Ϫ, 𝓐, 𝓑)
                elif c == ')':
                    𝓑, 𝓐, Ϫ = ⧖ζΨ(Ϫ, 𝓐, 𝓑)
                    𝓑, 𝓐, 𝓦[:] = ȸηλ(𝓑, 𝓐, 𝓦)
                else:
                    𝓑.append(c)
                ℘ += 1
            return 𝓑, 𝓐, Ϫ

        ψ, Ͻ, ᚧ = ᚧϽ(string_of_parentheses[𝓟:], ᚧ, ψ)
        𝓟 += 1

    return 𝓦