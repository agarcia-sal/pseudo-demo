from typing import List, Optional, Callable


def by_length(array_of_integers: List[int]) -> List[str]:
    def ξ₈₁μ(ʬ: int) -> Optional[str]:
        # Map integers 1-9 to their English words, else None
        return {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }.get(ʬ)

    def Ψ𝜋𝛌(Δφμ: List[int]) -> List[int]:
        if not Δφμ:
            return []
        ι𝔷𝚴 = Δφμ[0]
        𝚩𝒜 = Ψ𝜋𝛌(Δφμ[1:])
        if ι𝔷𝚴 < 0:
            return 𝚩𝒜
        return [ι𝔷𝚴] + 𝚩𝒜

    def 𝔯𝜔𝚷(τΣ𝒦: List[int]) -> List[int]:
        if not τΣ𝒦:
            return []
        α𝔾χ = τΣ𝒦[0]
        υδο = 𝔯𝜔𝚷(τΣ𝒦[1:])
        if not υδο or α𝔾χ >= υδο[0]:
            return [α𝔾χ] + υδο
        else:
            return [υδο[0]] + 𝔯𝜔𝚷([α𝔾χ] + υδο[1:])

    def ΩΩ(ζᚴ: List[int], ϰψ𝕨: Callable[[int], bool]) -> List[int]:
        if not ζᚴ:
            return []
        ζ = ζᚴ[0]
        ψ = ΩΩ(ζᚴ[1:], ϰψ𝕨)
        if ϰψ𝕨(ζ):
            return [ζ] + ψ
        else:
            return ψ

    def 匕ㄥχ(Ρ: List[int]) -> List[str]:
        return 匕ㄥχᴾ(Ρ, [])

    def 匕ㄥχᴾ(Ρ: List[int], ϼ: List[str]) -> List[str]:
        if not Ρ:
            return ϼ
        ρ = Ρ[0]
        ℓ = ξ₈₁μ(ρ)
        if ℓ is not None:
            return 匕ㄥχᴾ(Ρ[1:], ϼ + [ℓ])
        else:
            return 匕ㄥχᴾ(Ρ[1:], ϼ)

    υк = 𝔯𝜔𝚷(array_of_integers)
    return 匕ㄥχ(υк)