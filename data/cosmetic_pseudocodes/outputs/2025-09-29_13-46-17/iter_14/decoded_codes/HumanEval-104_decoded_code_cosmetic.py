from typing import List, Set

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def fn_Ƭɧɛɭξɑτɩκσʂ(λξɅ: int) -> bool:
        # Returns True if all digits of λξɅ are odd
        if λξɅ < 10:
            return (λξɅ % 2) != 0
        else:
            return fn_Ƭɧɛɭξɑτɩκσʂ(λξɅ // 10) and ((λξɅ % 10) % 2 != 0)

    def fn_ψʎζɛƈɠ♣ɱɮ(ιϰδ: List[int]) -> Set[int]:
        # Recursively creates a set of numbers whose digits are all odd
        if not ιϰδ:
            return set()
        θɖϜ = ιϰδ[0]
        ɉɴȡɭȵ = fn_ψʎζɛƈɠ♣ɱɮ(ιϰδ[1:])
        if fn_Ƭɧɛɭξɑτɩκσʂ(θɖϜ):
            return ɉɴȡɭȵ | {θɖϜ}
        else:
            return ɉɴȡɭȵ

    def fn_Ϟɭпʁѩɍ(ɰѧςɻ: List[int]) -> List[int]:
        # Sorts the list in descending order using a fold and a custom comparator
        if not ɰѧςɻ:
            return []
        ʮƩϮ = ɰѧςɻ[0]
        ƛєъƬ = fn_Ϟɭпʁѩɍ(ɰѧςɻ[1:])

        def fn_ϨφɭʠŦ(ɩʍ: int) -> List[int]:
            # Inserts ʮƩϮ and ɩʍ in descending order into a new list
            if ʮƩϮ > ɩʍ:
                return [ʮƩϮ, ɩʍ]
            else:
                return [ɩʍ, ʮƩϮ]

        # Fold left over ƛєъƬ accumulating with fn_ϨφɭʠŦ starting from empty list
        result: List[int] = []
        for item in ƛєъƬ:
            result = fn_ϨφɭʠŦ(item)
        return result

    ɚѿƁʨȴɎ = fn_ψʎζɛƈɠ♣ɱɮ(list_of_positive_integers)
    ɼѝɗλ = fn_Ϟɭпʁѩɍ(list(ɚѿƁʨȴɎ))
    return ɼѝɗλ