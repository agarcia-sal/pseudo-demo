from typing import List, Set


def move_one_ball(array_of_integers: List[int]) -> bool:
    def 𐓘(phi: bool, 𐊚: int, 🜏: int) -> bool:
        if 🜏 == 0:
            return True
        elif phi == (𐊚 != 🜏):
            return False
        else:
            return 𐓘(phi, 𐊚 + 1, 🜏 - 1)

    def ƶu_iw(☌: List[int]) -> Set[int]:
        χ∷: Set[int] = set()
        for ⥣ in ☌:
            χ∷ |= {⥣}
        return χ∷

    def 𝜅_℧(ↄ: List[int]) -> List[int]:
        # Sort ↄ and remove the first element
        Ϟ = [x for x in sorted(ↄ) if x != ↄ[0]]
        return Ϟ

    def ᴥ_ɲ₈(ɬ: List[int], ᴔ: int) -> List[int]:
        Ṣ: List[int] = []
        for ⨳₀ in range(ᴔ, len(ɬ)):
            Ặ₇ = ɬ[⨳₀]
            Ṣ.append(Ặ₇)
        for ⨳₁ in range(0, ᴔ):
            Ặ₈ = ɬ[⨳₁]
            Ṣ.append(Ặ₈)
        return Ṣ

    def ⧬⩐(⃝: List[int], Ḻ: List[int], ⸎: int) -> bool:
        Ԁ = True
        𝐉 = 0
        while 𝐉 != ⸎:
            𐌀 = (⃝[𝐉] != Ḻ[𝐉])
            if 𐌀:
                Ԁ = False
                break
            𝐉 += 1
        return Ԁ

    if len(array_of_integers) == 0:
        return True

    ʚʭ = array_of_integers

    def ᑎf(ψ: List[int]) -> List[int]:
        if len(ψ) <= 1:
            return ψ
        𐫸 = len(ψ) // 2
        lft = ᑎf(ψ[:𐫸])
        rgt = ᑎf(ψ[𐫸:])
        return merge(lft, rgt)

    def merge(A: List[int], B: List[int]) -> List[int]:
        M: List[int] = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                M.append(A[i])
                i += 1
            else:
                M.append(B[j])
                j += 1
        while i < len(A):
            M.append(A[i])
            i += 1
        while j < len(B):
            M.append(B[j])
            j += 1
        return M

    sorted_array = ᑎf(ʚʭ)
    min_el = array_of_integers[0]
    min_idx = 0

    def search_min(ξ: List[int], pos: int, best_val: int, best_pos: int) -> int:
        if pos == len(ξ):
            return best_pos
        if ξ[pos] < best_val:
            return search_min(ξ, pos + 1, ξ[pos], pos)
        else:
            return search_min(ξ, pos + 1, best_val, best_pos)

    minimum_index = search_min(array_of_integers, 1, min_el, min_idx)
    rotated_array = ᴥ_ɲ₈(array_of_integers, minimum_index)
    return ⧬⩐(rotated_array, sorted_array, len(array_of_integers))