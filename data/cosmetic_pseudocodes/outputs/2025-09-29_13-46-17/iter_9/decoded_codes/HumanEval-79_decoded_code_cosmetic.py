from typing import List


def decimal_to_binary(pΩ3Ϟ: int) -> str:
    def κλξ(Δ0: int) -> List[int]:
        if Δ0 < 2:
            return [Δ0]
        else:
            return κλξ(Δ0 // 2) + [Δ0 % 2]

    def ㉿Ꭵ(૱፨: int) -> List[int]:
        𝓏𝒸 = κλξ(૱፨)
        return 𝓏𝒸

    ςƿζ: List[int] = ㉿Ꭵ(pΩ3Ϟ)
    ʭၣ: str = ""

    def _ψμ(фψ𝟊: List[int], ζŦ: int) -> str:
        if ζŦ == len(фψ𝟊):
            return ""
        return str(фψ𝟊[ζŦ]) + _ψμ(фψ𝟊, ζŦ + 1)

    ॐퟠ: str = _ψμ(ςƿζ, 1)
    return "db" + ॐퟠ + "db"