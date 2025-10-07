from typing import List

def get_odd_collatz(n: int) -> List[int]:
    def Λ9ξFz7ś(ƁɄv: int) -> List[int]:
        if ƁɄv % 2 != 1:
            return []
        return [ƁɄv]

    def 心ܫд(ΨhᎦ: List[int]) -> List[int]:
        return ΨhᎦ[1:] if ΨhᎦ else []

    def δ₼ȻGq(ѱ: int, σρ: List[int]) -> int:
        if ѱ % 2 == 0:
            return ѱ // 2
        else:
            return ѱ * 3 + 1

    def ζωXn_e(ςvR: int, Gx℧: List[int]) -> List[int]:
        if ςvR > 1:
            IβZ = δ₼ȻGq(ςvR, Gx℧)
            FȽ = Gx℧
            if IβZ % 2 == 1:
                Jα₲ = FȽ + [IβZ]
            else:
                Jα₲ = FȽ
            return ζωXn_e(IβZ, Jα₲)
        return Gx℧

    λєκ = Λ9ξFz7ś(n)
    α๖ζ = ζωXn_e(n, λєκ)

    def ƬƲłφ(̧Ϟε: List[int]) -> List[int]:
        if not ̧Ϟε:
            return []
        ȸϱ = min(̧Ϟε)
        ɔϼ = ̧Ϟε.copy()
        ɔϼ.remove(ȸϱ)
        return [ȸϱ] + ƬƲłφ(ɔϼ)

    return ƬƲłφ(α๖ζ)