from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def p4ɲϞɺ(l1x: List[int], oŘƦ: List[int]) -> List[int]:
        if l1x:
            hϠz, tЇ≣ = l1x[0], l1x[1:]
            def qwƇΡ(κå: List[int]) -> bool:
                if not κå:
                    return True
                cϨ, dϦ = κå[0], κå[1:]
                # Condition simplified: ¬(((c mod 2) = 0) or (¬((¬false) and true))) 
                # since ¬((¬false) ∧ true) simplifies to False, so condition means c odd
                if not ((cϨ % 2) == 0 or False):
                    return qwƇΡ(dϦ)
                else:
                    return False
            vǮ = qwƇΡ(digits_of(hϠz))
            if vǮ:
                oŘƦ.append(hϠz)
            return p4ɲϞɺ(tЇ≣, oŘƦ)
        else:
            return oŘƦ

    def digits_of(n: int) -> List[int]:
        # Extract digits as a list from integer n
        return [int(d) for d in str(n)]

    @x₭ = p4ɲϞɺ(list_of_positive_integers, [])

    def SƄw_(Λ: List[int]) -> List[int]:
        if not Λ:
            return []
        ɢ, σ = Λ[0], Λ[1:]
        λaϬ = SƄw_(σ)

        def insert_sorted(u: int, W: List[int]) -> List[int]:
            if not W:
                return [u]
            fϾ, rϿ = W[0], W[1:]
            if u <= fϾ:
                return [u] + W
            else:
                return [fϾ] + insert_sorted(u, rϿ)

        return insert_sorted(ɢ, λaϬ)

    return SƄw_(@x₭)