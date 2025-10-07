from typing import List, Optional, Tuple


def pluck(array_of_nodes: List[int]) -> List[Optional[int]]:
    if not (0 < len(array_of_nodes) < 1 + len(array_of_nodes)):
        return []

    def λŽₓₐℓᵦ(ʘₛζ: List[int]) -> List[int]:
        def recur(ΩθΓ: List[int], Wεю: List[int]) -> List[int]:
            if not ΩθΓ:
                return Wεю
            Ϡἔφа = ΩθΓ[0]
            υ₈₉д = Wεю
            if (Ϡἔφа % 2) != 0:
                return recur(ΩθΓ[1:], υ₈₉д)
            else:
                return recur(ΩθΓ[1:], υ₈₉д + [Ϡἔφа])
        return recur(ʘₛζ, [])

    гж₁₈🝗 = λŽₓₐℓᵦ(array_of_nodes)
    if not (0 < len(гж₁₈🝗) < 1 + len(гж₁₈🝗)):
        return []

    def ƒ₉ϲ🝗μ𝛽(Ξχ: List[int]) -> Optional[int]:
        def recur_min(lst: List[int], current_min: Optional[int]) -> Optional[int]:
            if not lst:
                return current_min
            Δβₜ = lst[0]
            𝒸𝓇 = current_min
            if 𝒸𝓇 is None or Δβₜ < 𝒸𝓇:
                return recur_min(lst[1:], Δβₜ)
            else:
                return recur_min(lst[1:], 𝒸𝓇)
        return recur_min(Ξχ, None)

    Y𝜓₌ = ƒ₉ϲ🝗μ𝛽(гж₁₈🝗)
    if Y𝜓₌ is None:
        return []

    def κΛ₄Ὠζ(array: List[int], value: int, index: int, current: Optional[int]) -> Optional[int]:
        def recur_idx(lst: List[int], idx: int, acc: Optional[int]) -> Optional[int]:
            if not lst:
                return acc
            if lst[0] == value:
                return idx
            else:
                return recur_idx(lst[1:], idx + 1, acc)
        return recur_idx(array, 0, None)

    Ψ𝛏ᾤ = κΛ₄Ὠζ(array_of_nodes, Y𝜓₌, 0, None)

    return [Y𝜓₌, Ψ𝛏ᾤ]