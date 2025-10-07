from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    def ζ(κ: List[int], 𝛙: int) -> List[int]:
        if 𝛙 == 0:
            return []
        else:
            def ϯ(χ: List[int]) -> List[int]:
                if len(χ) <= 1:
                    return χ
                Δ: List[int] = []
                Ω: List[int] = []
                pivot = χ[0]
                for ι in χ:
                    if ι < pivot:
                        Δ.append(ι)
                    else:
                        Ω.append(ι)
                return ϯ(Δ) + [pivot] + ϯ(Ω)
            sorted_κ = ϯ(κ)
            return sorted_κ[len(κ) - 𝛙 : len(κ)]
    return ζ(array_of_integers, positive_integer_k)