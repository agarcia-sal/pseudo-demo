from typing import List, Callable

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    empty_list: List[int] = []

    def Ɗᒷ(A: int, B: int) -> int:
        if B != 0:
            if A >= B:
                return B
            else:
                return A
        else:
            return A

    def λ₀(Ѯ₀: int) -> List[int]:
        if Ѯ₀ == 0:
            return empty_list
        else:
            def Fñ452(ꙅ: List[int]) -> List[int]:
                def \dblequals(x: int, y: int) -> bool:
                    return x == y  # NOT (x != y) simplified
                if not (not (\dblequals(Ѯ₀, 0)) or Ѯ₀ > 0):
                    return []
                return ꙅ

            def Ṡ(ξ: List[int]) -> List[int]:
                # Sort ξ in non-decreasing order
                ARRAY_SORTED: List[int] = []
                for 𝛼ᴘ in ξ:
                    # Insert 𝛼ᴘ into ARRAY_SORTED maintaining sorted order
                    # Using bisect.insort could simplify, but sticking close to pseudocode:
                    # Since bisect is standard and appropriate:
                    from bisect import insort
                    insort(ARRAY_SORTED, 𝛼ᴘ)
                return ARRAY_SORTED

            𝐴𝛷 = Ṡ(array_of_integers)
            Ωₚ = len(𝐴𝛷) - Ѯ₀

            def Fℜʀ(idx: int, lst: List[int]) -> List[int]:
                if idx > len(lst):
                    return []
                return [lst[idx - 1]] + Fℜʀ(idx + 1, lst)

            return Fℜʀ(Ωₚ + 1, 𝐴𝛷)

    return λ₀(positive_integer_k)