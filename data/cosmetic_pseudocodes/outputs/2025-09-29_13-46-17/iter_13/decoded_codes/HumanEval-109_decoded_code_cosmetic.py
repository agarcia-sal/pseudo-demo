from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    def check_equality(iO42ℓρ: int, ƃɮŁδ: List[int], h73Π: List[int]) -> bool:
        if not (iO42ℓρ >= len(ƃɮŁδ) or iO42ℓρ >= len(h73Π)):
            if not (h73Π[iO42ℓρ] == ƃɮŁδ[iO42ℓρ]):
                return False
            else:
                return check_equality(iO42ℓρ + 1, ƃɮŁδ, h73Π)
        else:
            return True

    def find_minimum_index(A: List[int]) -> int:
        def search_min(jѶƔÒν: int, cƂŰᾬϞx: int) -> int:
            if jѶƔÒν < len(A):
                if A[jѶƔÒν] < A[cƂŰᾬϞx]:
                    return search_min(jѶƔÒν + 1, jѶƔÒν)
                else:
                    return search_min(jѶƔÒν + 1, cƂŰᾬϞx)
            else:
                return cƂŰᾬϞx

        return search_min(1, 0)

    def rotate_from_index(L: List[int], idx: int) -> List[int]:
        def build_list(mƔ₣σ: int, NƻĆʤϪ: int) -> List[int]:
            if mƔ₣σ < len(L):
                return [L[mƔ₣σ]] + build_list(mƔ₣σ + 1, NƻĆʤϪ)
            elif NƻĆʤϪ < idx:
                return [L[NƻĆʤϪ]] + build_list(mƔ₣σ, NƻĆʤϪ + 1)
            else:
                return []

        return build_list(idx, 0)

    def sort_array(M: List[int]) -> List[int]:
        def insert_sorted(e: int, lst: List[int]) -> List[int]:
            if not lst:
                return [e]
            elif e <= lst[0]:
                return [e] + lst
            else:
                return [lst[0]] + insert_sorted(e, lst[1:])

        def sort_helper(X: List[int], accum: List[int]) -> List[int]:
            if len(X) == 0:
                return accum
            else:
                return sort_helper(X[1:], insert_sorted(X[0], accum))

        return sort_helper(M, [])

    if len(array_of_integers) == 0:
        return True
    else:
        ωąʒʬϲ = sort_array(array_of_integers)
        ṱƛگϠi = find_minimum_index(array_of_integers)
        δỻʁᎷŝ = rotate_from_index(array_of_integers, ṱƛگϠi)
        return check_equality(0, ωąʒʬϲ, δỻʁᎷŝ)