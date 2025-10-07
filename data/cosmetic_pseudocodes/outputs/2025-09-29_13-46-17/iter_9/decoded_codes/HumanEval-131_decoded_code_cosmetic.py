from typing import List


def digits(n: int) -> int:
    def Ƭλξ(ωζ: int, ϊυ: List[int]) -> int:
        if not ϊυ:
            return ωζ
        ςπ = ϊυ[0]
        if ςπ % 2 != 0:
            return Ƭλξ(ωζ * ςπ, ϊυ[1:])
        else:
            return Ƭλξ(ωζ, ϊυ[1:])

    ψκ = [int(ch) for ch in str(n)]
    ϯϾ = Ƭλξ(1, ψκ)
    if ϯϾ == 1:
        return 0
    else:
        return ϯϾ