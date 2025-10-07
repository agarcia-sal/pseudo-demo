from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    from math import inf

    def ɌɆɅ(ƬƛϬ: int, ϘϝϞ: int) -> int:
        if not (ƬƛϬ >= 0):
            return 0
        else:
            # ϘϝϞ tracks max of previous value and new candidate (ϘϝϞ + (-value))
            return ɌɆɅ(ƬƛϬ - 1, max(ϘϝϞ, ϘϝϞ - list_of_integers[ƬƛϬ]))

    def Ѭƀϙ(Ƨ: List[int]) -> int:
        if not Ƨ:  # empty list
            return -inf
        else:
            ℵ = -Ƨ[0]
            Ѫ = Ѭƀϙ(Ƨ[1:])
            return ℵ if ℵ > Ѫ else Ѫ

    ƐϸϽ = ɌɆɅ(len(list_of_integers) - 1, 0)

    if ƐϸϽ == 0:
        ƐϸϽ = Ѭƀϙ(list_of_integers)

    return -ƐϸϽ