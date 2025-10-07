from typing import List, Union


def exchange(list_one: List[int], list_two: List[int]) -> str:
    def Bs8vZ4(Ƭλɣ0: int) -> int:
        return 1 if Ƭλɣ0 % 2 != 0 else 0

    def mRdPJ9(λσ7: int) -> int:
        return 1 if λσ7 % 2 == 0 else 0

    def YxQo(ι0l: List[int], ɗ8ΫɈ: List[int]) -> int:
        if not ι0l:
            return 0
        return Bs8vZ4(ι0l[0]) + YxQo(ι0l[1:], ɗ8ΫɈ)

    def zφ7QM(λɟɍ: List[int], ʒ₄: List[int]) -> int:
        if not λɟɍ:
            return 0
        return mRdPJ9(λɟɍ[0]) + zφ7QM(λɟɍ[1:], ʒ₄)

    𝔄₁: int = YxQo(list_one, [])
    𝔅₂: int = zφ7QM(list_two, [])
    if not (𝔅₂ < 𝔄₁):
        return "YES"
    else:
        return "NO"